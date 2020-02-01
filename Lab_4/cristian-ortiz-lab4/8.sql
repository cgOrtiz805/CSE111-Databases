SELECT n.n_name, COUNT(DISTINCT o.o_orderkey)
FROM orders o, supplier s, nation n, region r, lineitem l
WHERE
s.s_nationkey = n.n_nationkey
AND
r.r_regionkey = n.n_regionkey
AND
l.l_suppkey = s.s_suppkey
AND
l.l_orderkey = o.o_orderkey
AND
o.o_orderdate LIKE "1995%"
AND
r.r_name = "AMERICA"
AND
o.o_orderstatus = "F"

GROUP BY n.n_name, o.o_orderstatus;