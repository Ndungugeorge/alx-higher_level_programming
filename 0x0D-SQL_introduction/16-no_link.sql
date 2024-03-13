-- Task 16
SELECT score, name FROM second_table WHERE NOT ISNULL(name) ORDER BY score DESC;
