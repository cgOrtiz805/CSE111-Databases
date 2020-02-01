SELECT COUNT(c_custkey)
FROM
    (SELECT c.c_custkey
    FROM customer c INNER JOIN orders ON c.c_custkey = o_custkey
    WHERE o_orderdate LIKE "1995-08%" group by c_name HAVING COUNT(*) <=2); 