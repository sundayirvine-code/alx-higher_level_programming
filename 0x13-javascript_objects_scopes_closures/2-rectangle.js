#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
      if (w <= 0 || h <= 0) {
        // Create empty object if either argument is not positive
        return {};
      }
  
      // Otherwise, initialize instance attributes
      this.width = w;
      this.height = h;
    }
  }
  