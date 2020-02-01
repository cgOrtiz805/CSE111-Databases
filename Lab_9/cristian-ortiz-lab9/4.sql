SELECT s_name, COUNT(p.p_partkey)
FROM partsupp ps, Q2, part p
WHERE
p.p_partkey = ps.ps_partkey
AND
s_nation = "BRAZIL"
AND
ps.ps_suppkey = s_suppkey
AND
p.p_size < 20
GROUP BY s_name;
