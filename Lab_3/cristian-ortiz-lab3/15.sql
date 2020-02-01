SELECT n.n_name, substr(o.o_orderdate,1,4), COUNT(*)
FROM orders o, supplier s, nation n, lineitem l
WHERE 
s.s_nationkey = n.n_nationkey
AND
l.l_orderkey = o.o_orderkey
AND
l.l_suppkey = s.s_suppkey
AND 
o.o_orderpriority = "3-MEDIUM"
GROUP BY n.n_name, substr(o.o_orderdate,1,4);
