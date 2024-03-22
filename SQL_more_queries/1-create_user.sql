-- Creates the MySQL server user user_0d_1
-- Grants user_0d_1 with all privileges on local MySQL server
-- Sets the user_0d_1 password to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
