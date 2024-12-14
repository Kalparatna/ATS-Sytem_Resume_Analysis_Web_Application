-- Create database if not exists
CREATE DATABASE IF NOT EXISTS your_database_name;

-- Use the database
USE your_database_name;

-- Create table to store applicant data
CREATE TABLE IF NOT EXISTS applicant_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    mobile VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL,
    education VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    mode ENUM('Offline', 'Online') NOT NULL,
    type ENUM('Fulltime', 'Parttime') NOT NULL,
    score DECIMAL(5, 2), -- Adjust precision and scale for percentages
    resume_text LONGTEXT NOT NULL
);