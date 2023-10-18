-- List all tables in the specified database
SELECT TABLE_NAME
FROM information_schema.tables
WHERE TABLE_SCHEMA = DATABASE();