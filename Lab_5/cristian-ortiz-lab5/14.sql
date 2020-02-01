SELECT sr.r_name, cr.r_name ,substr(l.l_shipdate,1,4), SUM(l.l_extendedprice * (1-l.l_discount)) AS gross
FROM lineitem l 
INNER JOIN orders o ON o.o_orderkey = l.l_orderkey
INNER JOIN customer c ON c.c_custkey = o.o_custkey
INNER JOIN supplier s ON s.s_suppkey = l.l_suppkey
INNER JOIN nation sn ON sn.n_nationkey = s.s_nationkey
INNER JOIN region sr ON sn.n_regionkey = sr.r_regionkey
INNER JOIN nation cn ON cn.n_nationkey = c.c_nationkey
INNER JOIN region cr ON cn.n_regionkey = cr.r_regionkey
WHERE 
l.l_shipdate BETWEEN "1995-01-01" AND "1996-12-31"
GROUP BY sr.r_name, cr.r_name, substr(l.l_shipdate,1,4);

 




--FROM nation sn, nation cn, region sr, region cr, lineitem l, customer c, supplier s, orders o
