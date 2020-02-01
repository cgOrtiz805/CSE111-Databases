SELECT DISTINCT n.n_name
FROM nation n, customer c, orders o
WHERE c.c_nationkey = n.n_nationkey
AND
c.c_custkey = o.o_custkey
AND o.o_orderdate LIKE "1996-12-%";
