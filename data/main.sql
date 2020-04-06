create database if not exists test;
CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255));
INSERT INTO customers (name, address) VALUES ("john", "test");
