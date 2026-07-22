-- Assignment #7
-- Task
/*
Write THREE queries:
1. Find average Age, average Fare, MIN Fare, MAX Fare, and COUNT — all passengers, no grouping
2. Group by Pclass — find average Age, average Fare, total passengers per class
3. Group by Sex — find average Fare and average Age for male vs female
Which class paid the highest average fare? Write as a comment.
*/
-- Begin your work here
-- Query 1
SELECT ROUND(AVG(Age), 2) AS AverageAge, ROUND(AVG(Fare), 2) AS AverageFare,
       MIN(Fare) AS MinimumFare, MAX(Fare) As MaximumFare,
       COUNT(*) AS Total_Passengers
FROM passengers;

-- Query 2
SELECT Pclass, COUNT(*) AS Total_Passengers,
       ROUND(AVG(Age), 2) AS AverageAge, ROUND(AVG(Fare), 2) AS AverageFare
FROM passengers
GROUP BY Pclass;

-- Query 3
SELECT Sex, ROUND(AVG(Age), 2) AS AverageAge, ROUND(AVG(Fare), 2) AS AverageFare
FROM passengers
GROUP BY Sex;
-- Pclass 1 paid the highest average fare
