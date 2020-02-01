SELECT s.s_name, s.s_acctbal
FROM supplier s, region r, nation n
WHERE s.s_nationkey = n.n_nationkey
AND
r.r_regionkey = n.n_regionkey
AND
r.r_name = "ASIA"
AND s.s_acctbal > 1000;
