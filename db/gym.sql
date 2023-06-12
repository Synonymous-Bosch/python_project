DROP TABLE IF EXISTS members_gym_classes;
DROP TABLE IF EXISTS gym_classes; 
DROP TABLE IF EXISTS members;

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    duration INT NOT NULL,
    max_capacity INT NOT NULL,
    active BOOLEAN
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth DATE NOT NULL,
    premium BOOLEAN,
    active BOOLEAN
);

CREATE TABLE members_gym_classes (
    id SERIAL PRIMARY KEY,
    gym_class_id INT NOT NULL REFERENCES gym_classes(id),
    member_id INT NOT NULL REFERENCES members(id)
);