#!/bin/bash
set -e

PROTO_DIR="./proto"
OUT_DIR="./generated"


mkdir -p "$OUT_DIR/cpp"
mkdir -p "$OUT_DIR/python"
mkdir -p "$OUT_DIR/typescript"


echo "Cleaning old generated files..."
rm -rf "$OUT_DIR/cpp/"* "$OUT_DIR/python/"* "$OUT_DIR/typescript/"*

PROTO_FILES=$(find "$PROTO_DIR" -type f -name "*.proto")

if [ -z "$PROTO_FILES" ]; then
  echo "Error: No .proto files found in $PROTO_DIR"
  exit 1
fi

echo "Compiling Protobuf files for C++, Python, and TypeScript..."

protoc \
  --proto_path="$PROTO_DIR" \
  --cpp_out="$OUT_DIR/cpp" \
  --python_out="$OUT_DIR/python" \
  --pyi_out="$OUT_DIR/python" \
  --ts_out="$OUT_DIR/typescript" \
  $PROTO_FILES

echo "Done! Compiled outputs placed in $OUT_DIR/"