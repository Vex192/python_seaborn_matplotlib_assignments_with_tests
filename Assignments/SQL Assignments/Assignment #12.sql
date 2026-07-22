-- Assignment #12
-- Task
/*
Write TWO queries:
1. Find the class with the highest average fare. Use a subquery in FROM that first calculates average
fare per class — then SELECT top 1 from that result.
2. Find all three classes ranked by survival rate. Use a subquery in FROM that calculates survival rate
per class — then show all ranked descending.
Which class had both the highest fare AND highest survival rate? Write as a comment.
*/
-- Begin your work here
-- Query 1
SELECT Pclass, AverageFare
FROM (
    SELECT Pclass, ROUND(AVG(Fare), 2) AS AverageFare
    FROM passengers
    GROUP BY Pclass
)
ORDER BY AverageFare DESC
LIMIT 1;

-- Query 2
SELECT Pclass, SurvivalRate
FROM (
    SELECT Pclass, ROUND(AVG(Survived) * 100, 2) AS SurvivalRate
    FROM passengers
    GROUP BY Pclass
)
ORDER BY SurvivalRate DESC;

/*
No class had both highest. Pclass 1 had highest average fare while pclass 2 had highest
suvival Rate
*/
