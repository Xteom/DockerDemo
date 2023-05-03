-- Create the 'employees' table
CREATE TABLE
    employees (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        hire_date DATE NOT NULL
    );

-- Insert sample data into the 'employees' table
INSERT INTO
    employees (first_name, last_name, email, hire_date)
VALUES
    (
        'John',
        'Doe',
        'john.doe@example.com',
        '2021-01-01'
    ),
    (
        'Jane',
        'Doe',
        'jane.doe@example.com',
        '2021-02-01'
    ),
    (
        'Alice',
        'Smith',
        'alice.smith@example.com',
        '2021-03-01'
    ),
    (
        'Bob',
        'Johnson',
        'bob.johnson@example.com',
        '2021-04-01'
    );