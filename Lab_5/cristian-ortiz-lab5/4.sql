SELECT n.n_name, COUNT(DISTINCT c.c_custkey), COUNT(DISTINCT s.s_suppkey)
FROM supplier s, customer c, nation n, region r
WHERE 

c.c_nationkey  = n.n_nationkey
AND
s.s_nationkey = n.n_nationkey

AND
r.r_regionkey = n.n_regionkey
AND
r.r_name = "EUROPE"
GROUP BY n.n_name;
