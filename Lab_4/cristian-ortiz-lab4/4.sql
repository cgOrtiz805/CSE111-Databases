SELECT s.s_name, COUNT(p.p_partkey)
FROM partsupp ps, supplier s, nation n, part p
WHERE
p.p_partkey = ps.ps_partkey
AND
s.s_nationkey = n.n_nationkey
AND
n.n_name = "BRAZIL"
AND
ps.ps_suppkey = s.s_suppkey
AND
p.p_size < 20
GROUP BY s.s_name;
