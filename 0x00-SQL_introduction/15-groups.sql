-- lists the number of records w the same score from second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
