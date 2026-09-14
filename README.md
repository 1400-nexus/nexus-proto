# `nexus-proto` — Shared Data Contracts

This repository serves as the central source of truth for all Protocol Buffer schemas used across our microservices. It contains raw `.proto` definitions in `proto/` and pre-compiled bindings for C++, Python, and TypeScript in `generated/`.

---

## 🛠️ Prerequisites (For Schema Maintainers)

If you only **consume** generated types in your microservice, you do **not** need any tools installed besides Git.

If you are **adding or editing** `.proto` files and running the compilation scripts, install:

1. **Protobuf Compiler (`protoc`)**:
* **Linux**: `sudo apt install protobuf-compiler`
* **macOS**: `brew install protobuf`
* **Windows**: Download the binary zip from [Google Protobuf Releases](https://github.com/protocolbuffers/protobuf/releases), extract it, and add the `bin` folder to your system `PATH`.


2. **TypeScript Protoc Plugin (`ts-proto`)**:
* Run: `npm install -g protoc-gen-ts`



---

## 🚀 How to Compile Schemas

Whenever you add or modify a file inside `proto/`, run the compilation script matching your OS from the root of this repository:

* **Linux / macOS:**
```bash
./compile.sh
```


* **Windows (Command Prompt / PowerShell):**
```cmd
compile.bat
```



This script will automatically clear old outputs and generate updated C++, Python, and TypeScript files into `generated/`.

---

## 🧠 Understanding Git Submodules

### What is a Git Submodule?

A Git Submodule is simply a pointer embedded inside your microservice repository that targets a **specific commit** of this `nexus-proto` repository.

* It lives in a folder inside your microservice (e.g., `libs/nexus-proto`).
* It guarantees that every developer and service uses the exact same contract definitions without copy-pasting code.

---

## 🔄 Git Submodule Workflow Guide

### 1. Adding `nexus-proto` to a New Microservice

Run this command once inside your microservice repository:

```bash
git submodule add <REPO_URL_TO_NEXUS_PROTO> libs/nexus-proto
git commit -m "Add nexus-proto submodule"
```

### 2. Cloning a Microservice (First Time Setup)

When pulling a microservice repository that already has `nexus-proto` attached, run:

```bash
# Option A: Clone with submodules automatically
git clone --recurse-submodules <SERVICE_REPO_URL>

# Option B: If you already cloned without submodules
git submodule update --init --recursive
```

### 3. Pulling Latest Proto Changes into Your Service

When a teammate updates a contract in `nexus-proto` and you want the latest code in your microservice:

```bash
git submodule update --remote --merge
```

*Then, commit the updated submodule reference in your main service repo:*

```bash
git add libs/nexus-proto
git commit -m "Update nexus-proto submodule to latest version"
```

### 4. Updating a Schema (Modifying or Adding `.proto` Files)

When **you** need to change a contract:

```bash
# 1. Navigate into the submodule directory
cd libs/nexus-proto

# 2. Edit or add your .proto file in proto/

# 3. Run the compiler script
./compile.sh       # or compile.bat on Windows

# 4. Commit and push directly to nexus-proto
git add .
git commit -m "Add UserProfile message to user.proto"
git push origin main

# 5. Move back to your microservice root folder
cd ../..

# 6. Commit the updated submodule reference in your microservice
git add libs/nexus-proto
git commit -m "Bump nexus-proto submodule"
git push
```

---

## 💻 How to Use Generated Files in Services

### 1. C++ Service

Tell CMake to include the `generated/cpp` folder in your build:

```cmake
# CMakeLists.txt
target_include_directories(my_cpp_service PRIVATE 
    ${CMAKE_CURRENT_SOURCE_DIR}/libs/nexus-proto/generated/cpp
)
```

In your C++ code:

```cpp
#include "common/status.pb.h"
#include "auth/user.pb.h"

nexus::common::StatusCode code = nexus::common::SUCCESS;
```

---

### 2. TypeScript / Node.js Service

Import generated `.ts` files directly using relative paths (or configure path aliases in `tsconfig.json`):

In your TypeScript code:

```typescript
import { StatusCode } from './libs/nexus-proto/generated/typescript/common/status';
import { User } from './libs/nexus-proto/generated/typescript/auth/user';

const userStatus: StatusCode = StatusCode.SUCCESS;
```

---

### 3. Python Service

Add the `generated/python` directory to your Python path:

```python
import sys
import os

# Add generated folder to python import path
sys.path.append(os.path.abspath("libs/nexus-proto/generated/python"))

from common import status_pb2
from auth import user_pb2

status = status_pb2.SUCCESS
```