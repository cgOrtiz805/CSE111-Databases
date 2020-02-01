SELECT sr.r_name, cr.r_name, SUM(l.l_extendedprice)
FROM region sr, region cr, nation sn,nation cn, lineitem l, supplier s, customer c, orders o
WHERE 
o.o_orderkey = l.l_orderkey
AND
c.c_custkey = o.o_custkey
AND
l.l_suppkey = s.s_suppkey



AND
s.s_nationkey = sn.n_nationkey
AND
sn.n_regionkey = sr.r_regionkey






AND
c.c_nationkey = cn.n_nationkey
AND
cr.r_regionkey = cn.n_regionkey
GROUP BY sr.r_name, cr.r_name
;