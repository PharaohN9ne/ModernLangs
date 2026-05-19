--Exercise 1

SELECT
    ARRAY['apple', 'papaya', 'dragonfruit'] AS favorite_foods,
    ARRAY['apple', 'papaya', 'dragonfruit'][1] AS first_item,
    ARRAY['apple', 'papaya', 'dragonfruit'][3] AS last_item;

-- Exercise 2

SELECT
    'Morty' AS name,
    25 AS age,
    true AS wants_web_apps;

-- Exercise 3

SELECT jsonb_build_object(
               'title', 'Anthony',
               'author', 'Tony',
               'pages', 4532
       ) AS book;

-- Exercise 4

SELECT title, pages
FROM books;

-- Exercise 5

SELECT jsonb_build_object(
               'name', 'Alex',
               'languages', jsonb_build_array('English', 'Spanish', 'Python'),
               'active', true
       ) AS student;