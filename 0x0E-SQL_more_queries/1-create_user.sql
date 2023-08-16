-- creates the MySQL server user user_0d_1 and grant all priviledges and password user_0d_1_pwd
-- user_0d_1 must have all privileges on your MySQL server

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
