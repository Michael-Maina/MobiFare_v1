-- prepares a MySQL server for the project
DROP DATABASE IF EXISTS mobifare_dev_db;

CREATE DATABASE IF NOT EXISTS mobifare_dev_db;
CREATE USER IF NOT EXISTS 'mobifare_dev'@'localhost' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON `mobifare_dev_db`.* TO 'mobifare_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'mobifare_dev'@'localhost';
FLUSH PRIVILEGES;

USE mobifare_dev_db;

DROP TABLE IF EXISTS users;

CREATE TABLE `users` (
  `id` VARCHAR(60),
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
)
