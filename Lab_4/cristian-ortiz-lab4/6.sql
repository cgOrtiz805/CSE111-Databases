SELECT p.p_mfgr, o.o_orderpriority, COUNT(o.o_orderkey)

FROM part p, orders o, lineitem l, partsupp ps
WHERE
p.p_partkey = ps.ps_partkey
AND
l.l_partkey = ps.ps_partkey
AND
l.l_orderkey = o.o_orderkey
AND
ps.ps_suppkey = l.l_suppkey

GROUP BY p.p_mfgr, o.o_orderpriority;

