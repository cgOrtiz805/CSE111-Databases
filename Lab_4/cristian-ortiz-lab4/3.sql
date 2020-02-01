SELECT n.n_name, COUNT(o.o_orderkey)
FROM customer c, region r, orders o, nation n
WHERE
n.n_regionkey = r.r_regionkey
AND
c.c_nationkey = n.n_nationkey
AND
c.c_custkey = o.o_custkey
AND
r.r_name = "EUROPE"
GROUP BY n.n_name;
