SELECT s_region,s_name
FROM Q2
GROUP BY s_region
HAVING MAX(s_acctbal)
;
