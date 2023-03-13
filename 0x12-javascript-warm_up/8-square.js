#!/usr/bin/node

const arg = process.argv[2];

if (!isNaN(arg) && Number.isInteger(Number(arg))) {
  const size = parseInt(arg);

  for (let i = 0; i < size; i++) {
    console.log("X".repeat(size));
  }
} else {
  console.log("Missing size");
}
