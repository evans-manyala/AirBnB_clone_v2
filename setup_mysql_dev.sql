-- Prepares the MySQL server for the project
-- Creates a database hbnb_dev_db (in the MySQL server)
-- Creates a new user hbnb_dev (in the MySQL server)
-- The user hbnb_dev has all privileges granted on the database hbnb_dev_db (in the MySQL server)

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;


CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT
SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

