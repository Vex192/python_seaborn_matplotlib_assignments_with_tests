-- Task 3
/*
Write ONE complete query that builds a passenger profile report.
Your query must show ALL of these columns:
1. Name
2. Sex
3. Age — but use COALESCE to show 0 wherever Age is NULL
4. Pclass
5. TicketClass column using CASE WHEN:
• "First Class" if Pclass = 1
• "Second Class" if Pclass = 2
• "Third Class" if Pclass = 3
6. SurvivalStatus column:
• "Survived" if Survived = 1
• "Did Not Survive" if Survived = 0
7. FamilySize = SibSp + Parch + 1
8. FareCategory column:
• "Expensive" if Fare > 50
• "Moderate" if Fare > 20
• "Cheap" if Fare <= 20
Sort by: Pclass ascending, then Fare descending
Then write a SECOND query — a summary:
• Group by TicketClass and SurvivalStatus
• Show: TicketClass, SurvivalStatus, count of passengers
• Sort by TicketClass, then count descending
Write 2 sentences as comments:
What pattern do you notice about survival and ticket class?
*/
-- Query 1
SELECT Name, 
       Sex, 
       COALESCE(Age, 0) AS AgeOrZero,
       Pclass,
       CASE
           WHEN Pclass = 1 THEN 'First Class'
           WHEN Pclass = 2 THEN 'Second Class'
           WHEN Pclass = 3 THEN 'Third Class'
           ELSE 'Unknown'
       END AS TicketClass,
       CASE
           WHEN Survived = 1 THEN 'Survived'
           WHEN Survived = 0 THEN 'Did Not Survive'
           ELSE 'Unknown'
       END AS SurvivalStatus,
       (Sibsp + Parch + 1) AS FamilySize,
       CASE
           WHEN Fare > 50 THEN 'Expensive'
           WHEN Fare > 20 THEN 'Moderate'
           WHEN Fare <= 20 THEN 'Cheap'
           ELSE 'Unknown'
       END AS FareCategory
FROM passengers
ORDER BY Pclass ASC, Fare DESC;

-- Query 2
SELECT
       COUNT(*) AS PassengerCount,
       CASE
           WHEN Pclass = 1 THEN 'First Class'
           WHEN Pclass = 2 THEN 'Second Class'
           WHEN Pclass = 3 THEN 'Third Class'
           ELSE 'Unknown'
       END AS TicketClass,
       CASE
           WHEN Survived = 1 THEN 'Survived'
           WHEN Survived = 0 THEN 'Did Not Survive'
           ELSE 'Unknown'
       END AS SurvivalStatus
FROM passengers
GROUP BY TicketClass, SurvivalStatus
ORDER BY TicketClass, PassengerCount DESC;
/*
Passengers who have a lower ticket class survive less as compared to higher ticket class
like first class. Also alot of passengers don't survive in third class which proves this.
*/
