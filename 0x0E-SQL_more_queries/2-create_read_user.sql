-- Create the database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create or update user user_0d_2 and grant SELECT privilege
CREATE OR REPLACE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant USAGE on all databases and SELECT on hbtn_0d_2
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';