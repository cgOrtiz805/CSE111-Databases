SELECT p.p_mfgr, o_orderpriority, COUNT(o_orderkey)
FROM part p, Q5, lineitem l, partsupp ps
WHERE
p.p_partkey = ps.ps_partkey
AND
l.l_partkey = ps.ps_partkey
AND
l.l_orderkey = o_orderkey
AND
ps.ps_suppkey = l.l_suppkey

GROUP BY p.p_mfgr, o_orderpriority;

