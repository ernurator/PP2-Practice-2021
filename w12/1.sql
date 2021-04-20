CREATE TABLE users (
    username VARCHAR(255),
    age INTEGER,
    joined DATE,
    hobby TEXT,
    password VARCHAR(255)
);

-- CRUD operations
-- Create, read, update, delete

-- Create

INSERT INTO users VALUES ('user 1', 13, '20-04-2021', 'some hobby', 'password');

INSERT INTO users VALUES ('user 2', 63, '20-04-2011', 'some hobby', 'password2'),
                         ('user 3', 1, '20-04-2020', 'some hobby', 'password3');

INSERT INTO users(username, password, age) VALUES ('user 4', 'asd', 133);

INSERT INTO users(username, password, age) VALUES ('user 5', 'asdd', 33)
RETURNING age;

-- Read

SELECT * FROM users;

SELECT username, password FROM users;

SELECT *
FROM users
WHERE age >= 15 AND joined IS NOT NULL;

-- Update

UPDATE users
SET password = 'new password 1'
WHERE age > 10 AND joined > '01-01-2019';

-- Delete

DELETE FROM users
WHERE username = 'user 3';
