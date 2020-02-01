
import sqlite3

def create_connection(db_connection):
    db_connection = None
    db_name = "C:/Users/cortiz42/Documents/CSE111/TPCH.db"
    try:
        db_connection = sqlite3.connect(db_name)
    except sqlite3.Error as err:
        print(err)


    if db_connection:
     print(db_connection)
     print("SUCCESS")
     print("\n\n")
    return db_connection

def create_table(db_connection):
    try:
        create = db_connection.cursor()
        create.execute("CREATE TABLE warehouse" +
                       "(w_warehousekey DECIMAL(3,0) not null, " +
                       "w_name CHAR(25) not null, " +
                       "w_supplierkey DECIMAL(2,0) not null," +
                       "w_capacity DECIMAL (6,2) not null, " +
                       "w_address varchar(40) not null, " +
                       "w_nationkey decimal(2,0) not null )")
    except sqlite3.Error as e:
        print(e)

def insert(db_connection):
    create = db_connection.cursor()
    a = input("Name: ")
    b = input("Supplier: ")
    c = input("Capacity: ")
    d = input("Address: ")
    e = input("Nation: ")
    e = e.upper()

    w_nationkey = None
    w_supplierkey = None
    w_warehousekey = None

    create.execute("SELECT COUNT(w_warehousekey) FROM warehouse")  ## Generates the Key
    w_warehousekey = create.fetchone()[0]  # makes it into a int
    w_warehousekey += 1

    create.execute("SELECT n_nationkey FROM nation WHERE n_name= '" + e + "';");  # Generates the Nationkey
    w_nationkey = create.fetchall()
    if w_nationkey == []:
        print(e + " Does not Exist in our DB")
        exit()

    for row in w_nationkey:
        row[0]

    create.execute("SELECT s_suppkey FROM supplier where s_name= '" + b + "';");  # Generates the supplier key
    w_supplierkey = create.fetchall()
    if w_supplierkey == []:
        print(b + " Does not Exist in our DB")
        exit()
    for supp in w_supplierkey:
        supp[0]

    try:  # INSERTS VALUES INTO DB
        create.execute("INSERT INTO warehouse  VALUES(" + "'" + str(w_warehousekey) + "'" + ", '" + a + "','" + str(
            supp[0]) + "','" + c + "','" + d + "','" + str(row[0]) + "'" + ");")
        db_connection.commit()
    except sqlite3.Error as e:
        print(e)


def query_1(db_connection):
    create = db_connection.cursor()
    create.execute("select s_name, min(m.s)  from " 
                   "( select s_name, count(s_name) s from supplier, warehouse "
                   "where w_supplierkey = s_suppkey "
                   "group by w_supplierkey)m;")
    query_1_result = create.fetchall()
    print("*************QUERY1 RESULT****************")
    for q1 in query_1_result:
        print(q1[0] + "   " + str(q1[1]))


def query_2(db_connection):
    create = db_connection.cursor()
    create.execute("SELECT MAX(w_capacity) FROM warehouse")  # ***************************Query 2**********************
    query_2_result = create.fetchall()
    for q2 in query_2_result:
        print("*************QUERY2 RESULT****************")
        print(q2[0])



def query_3(db_connection):
    create = db_connection.cursor()
    cap = input("warehouses in Europe with capacity < ")
    create.execute(
        "SELECT w_name FROM warehouse,nation, region where w_nationkey = n_nationkey and n_regionkey = r_regionkey"
        " AND r_name = 'EUROPE' AND w_capacity < '" + cap + "';")
    query_3_result = create.fetchall()
    print("*************QUERY3 RESULT****************")
    for q3 in query_3_result:
        print(q3[0])
def query_4(db_connection):
    create = db_connection.cursor()
    cap = input("Enter a Supplier name:")  # *****************QUERY 4******************************************
    print("*******************QUERY4 RESULT***********************")
    create.execute(
        "SELECT SUM(w_capacity) FROM supplier INNER JOIN warehouse ON s_suppkey = w_supplierkey WHERE s_name ='" + cap + "';")
    warehouse_cap = create.fetchall()[0]
    print("Total Warehouse Capacity: " + str(warehouse_cap[0]))

    create.execute(
        "SELECT SUM(ps_availqty) FROM partsupp INNER JOIN supplier ON s_suppkey = ps_suppkey WHERE s_name = '" + cap + "';")
    part_amount = create.fetchall()[0]
    print("Total Amount of Parts: " + str(part_amount[0]))

    if part_amount[0] <= warehouse_cap[0]:
        print("YES")
    else:
        print("NO")


def query_5(db_connection):
    create = db_connection.cursor()
    nat = input("Enter a Nation: ")  # ********************QUERY5*******************************************
    nat = nat.upper()
    create.execute("SELECT w_name FROM warehouse"
                   " INNER JOIN nation ON w_nationkey = n_nationkey"
                   " WHERE n_name='" + nat + "' GROUP BY w_name "
                                             "ORDER BY w_capacity DESC")
    query5 = create.fetchall()
    print("**************QUERY5 RESULT**************")
    for q5 in query5:
        print(q5[0])

def query_6(db_connection):
    create = db_connection.cursor()
    try:
        csup = input("Enter the a Supplier to be replaced: ")  # ***************QUERY 6**************************
        create.execute("SELECT s_suppkey FROM supplier WHERE s_name = '" + csup + "';")
        current = create.fetchall()[0]
        print(current[0])

        nsup = input("Enter the new Supplier: ")
        create.execute("SELECT s_suppkey FROM supplier WHERE s_name = '" + nsup + "';")
        new = create.fetchall()[0]
        print(new[0])
        create.execute(
            "UPDATE warehouse SET w_supplierkey ='" + str(new[0]) + "'WHERE w_supplierkey = '" + str(current[0]) + "';")
        #db_connection.commit()
        print("*****************QUERY 6 RESULTS*****************")
        print(csup + " successfully updated with " + nsup)
    except sqlite3.Error as error:
        print(error)

    create.execute("SELECT w_name, w_supplierkey FROM warehouse WHERE w_supplierkey = '" + str(new[0]) + "';")
    query6re = create.fetchall()
    print("List of updated Tuples")
    for q6 in query6re:
        print(str(q6[0]) + "  " + str(q6[1]))


def main():

 db_name = r"C:/Users/cortiz42/Documents/CSE111/TPCH.db"
 db_connection = create_connection(db_name)
 choice = input()






 create_table(db_connection)
 insert(db_connection)
 query_1(db_connection)
 query_2(db_connection)
 query_3(db_connection)
 query_4(db_connection)
 query_5(db_connection)
 query_6(db_connection)

 db_connection.close()
main()
