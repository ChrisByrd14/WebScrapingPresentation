-- DDL statement for creating a simple SQLite table
CREATE TABLE IF NOT EXISTS books (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  url TEXT,
  upc TEXT,
  price REAL NOT NULL DEFAULT 0.00,
  in_stock INTEGER NOT NULL DEFAULT 0
);

