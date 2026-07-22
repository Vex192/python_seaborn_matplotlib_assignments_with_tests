-- Assignment #5
-- Task
/*
Write TWO queries:
1. Add SurvivalStatus: 'Survived' if Survived=1, 'Did Not Survive' if Survived=0. Show: Name, Sex,
Pclass, SurvivalStatus. Sort by Pclass.
2. Add TicketClass: First/Second/Third Class. Add FareCategory: Expensive (>50), Moderate (>20), 
Cheap (<=20). Show Name, Fare, both new columns.
How many First Class passengers survived? Write as a comment.
*/
-- Begin your work here
-- Query 1
SELECT Name, Sex, Pclass,
    CASE
        WHEN Survived = 1 THEN 'Survived'
        WHEN Survived = 0 THEN 'Did Not Survive'
        ELSE 'Unknown'
    END AS SurvivalStatus
FROM passengers
ORDER BY Pclass ASC;

-- Query 2
SELECT Name, Fare,
    CASE
        WHEN Pclass = 1 THEN 'First Class'
        WHEN Pclass = 2 THEN 'Second Class'
        WHEN Pclass = 3 THEN 'Third Class'
        ELSE 'Unknown'
    END AS TicketClass,
    CASE
        WHEN Fare > 50 THEN 'Expensive'
        WHEN Fare > 20 THEN 'Moderate'
        WHEN Fare <= 20 THEN 'Cheap'
        ELSE 'Unknown'
    END AS FareCategory
FROM passengers;
-- Four First Class passengers survived
