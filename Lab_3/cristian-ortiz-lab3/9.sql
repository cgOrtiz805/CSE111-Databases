SELECT n.n_name, COUNT(*),ROUND(AVG(s.s_acctbal),11)
FROM nation n, supplier s
WHERE n.n_nationkey = s.s_nationkey
GROUP BY n.n_name
HAVING COUNT(*) >= 5;