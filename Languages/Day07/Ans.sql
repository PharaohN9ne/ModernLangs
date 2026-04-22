CREATE TABLE products (
                          product_name TEXT,
                          item_price NUMERIC,
                          quantity INT
);

INSERT INTO products (product_name, item_price, quantity)
VALUES
    ('basketball', 3.23, 25),
    ('soccer ball', 12.50, 4),
    ('tennis racket', 59.99, 2);

CREATE TABLE users (
                       name TEXT,
                       age INT,
                       role TEXT
);

INSERT INTO users (name, age, role)
VALUES
    ('Anthony', 32, 'viewer'),
    ('Maya', 17, 'editor'),
    ('Jordan', 45, 'admin');

--Exercise1
select
    'Anthony' AS name,
    32 as age,
    true as wants_web_apps;

--Exercise2
SELECT
    8 as password_length,
    case
        when 8 < 8 then 'Password too short'
        else 'Password length okay'
    END AS password_status;

--Exercise3
select product_name, quantity
from products;

--Exercise4
select
    100 as price,
    0.06 as tax_rate,
    100 + (100 * 0.06) as final_price;

--Exercise5
with course_info as (
    select 'PostgreSQL Basics' as course_name
)
select course_name
from course_info;