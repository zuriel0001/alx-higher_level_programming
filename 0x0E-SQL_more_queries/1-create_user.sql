-- Check if the user exists
SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' LIMIT 1;

-- If the user doesn't exist, create it
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
