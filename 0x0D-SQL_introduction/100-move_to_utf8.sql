-- Convert the entire database hbtn_0c_0 to UTF8
USE `hbtn_0c_0`;

-- Convert the table first_table to UTF8mb4
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;