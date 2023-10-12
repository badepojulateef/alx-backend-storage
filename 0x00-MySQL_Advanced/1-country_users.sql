-- Create the "users" table if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    -- Define the "id" column as an auto-incrementing primary key
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- Define the "email" column as a string with a maximum length of 255 characters, never null, and unique
    email VARCHAR(255) NOT NULL UNIQUE,
    -- Define the "name" column as a string with a maximum length of 255 characters
    name VARCHAR(255),
    -- Define the "country" column as an enumeration with default value "US" and limited to values 'US', 'CO', and 'TN'
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
