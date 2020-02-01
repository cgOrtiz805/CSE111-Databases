SELECT r.r_name, COUNT(c.c_acctbal)
FROM customer c
LEFT JOIN orders o ON c.c_custkey = o.o_custkey
INNER JOIN nation n ON c.c_nationkey = n.n_nationkey 
INNER JOIN region r ON r.r_regionkey = n.n_regionkey
WHERE
o.o_orderkey IS NULL
AND
c.c_acctbal > (SELECT AVG(c_acctbal) FROM customer)

GROUP BY r_name;