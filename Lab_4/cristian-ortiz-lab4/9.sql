SELECT COUNT(DISTINCT o.o_clerk)
FROM supplier s, nation n, orders o, lineitem l
WHERE
 s.s_nationkey = n.n_nationkey
AND
s.s_suppkey = l.l_suppkey
AND
l.l_orderkey = o.o_orderkey
AND

n.n_name = "RUSSIA";