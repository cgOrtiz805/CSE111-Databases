SELECT SUM(o.o_totalprice)
FROM orders o, customer c, nation n, region r
WHERE n.n_regionkey = r.r_regionkey
AND
n.n_nationkey = c.c_nationkey
AND
o.o_custkey = c.c_custkey
AND r.r_name = "EUROPE"
AND
o.o_orderdate LIKE "1996%";