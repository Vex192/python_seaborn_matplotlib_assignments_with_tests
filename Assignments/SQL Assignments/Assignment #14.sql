-- Assignment #14
-- Task
/*
Write TWO advanced queries:
1. Rank passengers by Fare within each Pclass using RANK() OVER (PARTITION BY Pclass ORDER
BY Fare DESC). Show: Pclass, Name, Fare, Rank. Filter to show only Rank 1 — highest fare per class.
2. Rank all passengers by Age within each Sex. Show top 3 oldest per sex.
Who paid the most in each class? Who is oldest male and oldest female? Write as comments.
*/
-- Begin your work here
-- Query 1
SELECT Pclass, Name, Fare, Rank
FROM (
    SELECT Pclass, Name, Fare,
           RANK() OVER (PARTITION BY Pclass ORDER BY Fare DESC) AS Rank
    FROM passengers
) AS Rank
WHERE Rank = 1;

-- Query 2
SELECT Sex, Name, Age, Rank 
FROM ( 
    SELECT Sex, Name, Age, 
           RANK() OVER (PARTITION BY Sex ORDER BY Age DESC) AS Rank 
    FROM passengers 
    GROUP BY Sex, Age
) AS Rank 
WHERE Rank <= 3;

/*
1st Class: Mrs. John Cumings, 
2nd Class: Mrs. Nicholas Nasser, 
3rd Class: Mrs. William Hewlett
*/
/*
Oldest female: Miss. Elizabeth Buss,
Oldest Male: Mr. Timothy McCarthy
*/

