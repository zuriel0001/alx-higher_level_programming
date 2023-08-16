-- Script that lists all privileges of the users user_0d_1 and user_0d_2.
SELECT * FROM mysql.user WHERE User IN ('user_0d_1', 'user_0d_2');
