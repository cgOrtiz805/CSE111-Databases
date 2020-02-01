SELECT COUNT(o.o_orderkey)
FROM orders o, customer c, nation n
WHERE o.o_custkey = c.c_custkey
AND
c.c_nationkey = n.n_nationkey
AND
n.n_name = "BRAZIL"
AND o.o_orderpriority = "1-URGENT"
AND
o_orderdate BETWEEN "1994-01-01" AND "1997-12-31"
;
