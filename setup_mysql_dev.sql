-- This is the database setup file for the project - taskwise 
-- To prepare a MySQL server for the taskwise project
-- User: taskwise_dev_dp
-- User password: taskwise_admin_app_pass
-- Host: localhost
-- database name : taskwise_dev_dp

-- Create the database
CREATE DATABASE IF NOT EXISTS taskwise_dev_dp ;

-- Create the user
CREATE USER IF NOT EXISTS 'taskwise_admin_app_dev'@'localhost' IDENTIFIED BY 'taskwise_admin_app_pass';


-- Grant that user all privileges on the taskwise_dev_dp database,
-- and grant SELECT privileges on the performance_schema database.

GRANT ALL PRIVILEGES ON taskwise_dev_dp.* TO 'taskwise_admin_app_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'taskwise_admin_app_dev'@'localhost';


FLUSH PRIVILEGES;
