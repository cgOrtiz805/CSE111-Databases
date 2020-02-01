SELECT s_region, MAX(s_acctbal)
FROM Q2

GROUP BY s_region;
