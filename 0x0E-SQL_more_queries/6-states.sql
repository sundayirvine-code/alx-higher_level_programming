-- creates the database hbtn_0d_usa and the table states 
-- (in the database hbtn_0d_usa) on your MySQL server.
-- If the table states already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE PRIMARY KEY NOT NULL AUTO = TRUE, name VARCHAR(256))
