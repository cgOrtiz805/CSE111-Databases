SELECT s_nation, COUNT(s_suppkey)
FROM Q2

GROUP BY s_nation
ORDER BY s_nation ASC;