
CREATE TRIGGER NegCheck
         AFTER UPDATE
            ON customer
            FOR EACH ROW
          WHEN OLD.c_acctbal <> NEW.c_acctbal
BEGIN
    UPDATE customer
       SET c_comment = 'Negative balance!!! Add money now!'
     WHERE c_acctbal < 0;
END;

CREATE TRIGGER PosCheck
         AFTER UPDATE
            ON customer
            FOR EACH ROW
          WHEN OLD.c_acctbal <> NEW.c_acctbal
BEGIN
    UPDATE customer
       SET c_comment = 'Returned to Positive Balance'
     WHERE c_acctbal > 0;
END;

UPDATE customer
   SET c_acctbal = -100
 WHERE c_nationkey IN (
    SELECT c_nationkey
      FROM customer
           INNER JOIN
           nation ON c_nationkey = n_nationkey
           INNER JOIN
           region ON n_regionkey = r_regionkey
     WHERE r_name = 'ASIA'
);

SELECT COUNT(c_custkey)
FROM customer INNER JOIN nation ON c_nationkey=n_nationkey
WHERE n_name = 'CHINA'
AND c_acctbal < 0;

UPDATE customer 
SET c_acctbal = 100
WHERE c_nationkey IN ( SELECT c_nationkey
      FROM customer
           INNER JOIN
           nation ON c_nationkey = n_nationkey
           WHERE n_name = 'JAPAN');

 SELECT COUNT(c_custkey)
      FROM customer
           INNER JOIN
           nation ON c_nationkey = n_nationkey
           INNER JOIN
           region ON n_regionkey = r_regionkey
     WHERE r_name = 'ASIA' aND c_acctbal < 0;