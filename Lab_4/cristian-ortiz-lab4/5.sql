SELECT c.c_name, COUNT(o.o_orderkey)
FROM nation n, orders o, customer c
WHERE
c.c_nationkey = n.n_nationkey
AND
c.c_custkey = o.o_custkey
AND
n.n_name = "GERMANY"
AND
o.o_orderdate LIKE "1995%"
GROUP BY
c.c_name;
