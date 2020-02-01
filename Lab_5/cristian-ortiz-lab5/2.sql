SELECT r_name, COUNT(s_suppkey)
FROM nation 
 INNER JOIN supplier ON s_nationkey = n_nationkey
  INNER JOIN region r ON n_regionkey = r.r_regionkey
WHERE

s_acctbal > (SELECT AVG(s_acctbal) FROM nation INNER JOIN supplier ON s_nationkey = n_nationkey INNER JOIN region rr ON n_regionkey = rr.r_regionkey
 WHERE r.r_name =rr.r_name
GROUP BY r_name)
GROUP BY r_name;