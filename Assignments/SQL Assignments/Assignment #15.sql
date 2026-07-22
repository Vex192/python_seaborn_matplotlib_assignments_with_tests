-- Assignment #15
-- Task
/*
Write TWO queries:
1. Calculate a running total of Fare ordered by PassengerId. Show: PassengerId, Name, Fare,
RunningFareTotal = SUM(Fare) OVER (ORDER BY PassengerId).
2. Calculate a running count of survivors ordered by PassengerId. Show: PassengerId, Survived,
RunningSurvivors = SUM(Survived) OVER (ORDER BY PassengerId).
What is the total fare from all 30 passengers? The last row of your running total shows this. Write as a
comment.
*/
-- Begin your work here
-- Query 1
SELECT PassengerId, Name, Fare, 
       SUM(Fare) OVER (ORDER BY PassengerID) AS RunningFareTotal 
FROM passengers;

-- Query 2
SELECT PassengerId, Survived, 
       SUM(Survived) OVER (ORDER BY PassengerId) AS RunningSurvivors
FROM passengers;

-- Total Fare = 636.09