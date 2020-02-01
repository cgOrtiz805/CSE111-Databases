SELECT n.n_name, o.o_orderstatus, COUNT(o.o_orderkey)
FROM customer c, region r, nation n, orders o
WHERE
c.c_custkey = o.o_custkey
AND
c.c_nationkey = n.n_nationkey
AND
n.n_regionkey = r.r_regionkey
AND
r.r_name = "ASIA"


GROUP BY n.n_name, o.o_orderstatus;