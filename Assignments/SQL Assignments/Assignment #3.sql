-- Assignment #3
-- Task
/*
Write FOUR queries:
1. Show all passengers sorted by Fare from highest to lowest
2. Show top 5 who paid highest Fare — Name and Fare only
3. Show 5 youngest passengers — Name and Age (exclude NULLs)
4. Sort by Pclass ascending, then Fare descending within each class
Who paid the highest fare? What class were they in? Write as a comment.
*/
-- Begin your work here
-- Query 1
SELECT *
FROM passengers
ORDER BY Fare DESC;

-- Query 2
SELECT Name, Fare
FROM passengers
ORDER BY Fare DESC
LIMIT 5;

-- Query 3
SELECT Name, Age
FROM passengers
WHERE Age IS NOT NULL
ORDER BY Age ASC
LIMIT 5;

-- Query 4
SELECT *
FROM passengers
ORDER BY Pclass ASC, Fare DESC;


