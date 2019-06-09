CREATE DATABASE hackathon;

USE hackathon;

CREATE TABLE post
(
    id INT auto_increment PRIMARY KEY,
    bus_id INT NOT NULL,
    message TEXT NULL,
    user_id   INT NULL,
    published tinyint DEFAULT 1 NOT NULL
);

