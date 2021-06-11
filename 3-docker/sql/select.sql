-- in sql, -- is a comment
-- SELECT is the one command that returns any data

SELECT 1;
SELECT 2 + 2;
SELECT current_time;
SELECT extract(hour from current_time);

SELECT 2 + 2, 4;
-- 4, 4

-- with the FROM clause of the SELECT statement,
-- you specify a table
SELECT title, id, 2 + 2
FROM films;

SELECT id, title || ' (' || release_year || ')' AS movie
FROM films;

-- WHERE clause
SELECT id, title || ' (' || release_year || ')' AS movie
FROM films
WHERE title < 'b' OR title > 'x';

-- < <= > >= =
-- != <>
-- generally in SQL, everything is case-insensitive at least by default

-- SELECT statement
-- for making queries to the database (read access, not modifying)
-- made up of several "clauses", six main ones
SELECT *
FROM genres
WHERE LENGTH(name) < 6;

-- we've seen
-- 1. SELECT clause (chooses which columns will be returned)
-- 2. FROM clause (chooses which table to access)
-- 3. WHERE clause (filters rows based on conditions)

-- we have the ability to "aggregate" rows together
-- using "GROUP BY" clause, together with aggregate functions.
-- we have a handful of built-in aggregate functions:
--   SUM, COUNT, AVG, MIN, MAX
SELECT state, COUNT(*), SUM(id)
FROM customers
GROUP BY state;

-- when we use GROUP BY, we can only select columns
-- that are either *part* of the GROUP BY, or,
-- are aggregated

-- the next clause that SELECT has is HAVING

-- list states by how many customers, if at least 2 customers
SELECT state, COUNT(*)
FROM customers
WHERE state IS NOT NULL
-- WHERE filters before the grouping
GROUP BY state
HAVING COUNT(*) >= 2;
-- HAVING filters after the grouping

-- last clause is ORDER BY
-- list states by how many customers, if at least 2 customers,
--    sort states alphabetically
SELECT state, COUNT(*) AS number
FROM customers
WHERE state IS NOT NULL
GROUP BY state
HAVING COUNT(*) >= 2
ORDER BY state;

-- the logical order of execution of the clauses of SELECT:
--  1. FROM
--  2. WHERE
--  3. GROUP BY
--  4. HAVING
--  5. SELECT
--  6. ORDER BY
