#!/usr/bin/node

function add(a, b) {
    return a + b;
  }
  
  const arg1 = process.argv[2];
  const arg2 = process.argv[3];
  
  if (!isNaN(arg1) && !isNaN(arg2)) {
    const num1 = parseInt(arg1);
    const num2 = parseInt(arg2);
    
    console.log(add(num1, num2));
  } else {
    console.log("Invalid arguments");
  }
  