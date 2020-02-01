import time
import sqlite3

db_connection = None
db_name = r"C:/Users/cortiz42/Documents/CSE111/Project/Pokedex.db"
try:
    db_connection = sqlite3.connect(db_name)
except sqlite3.Error as err:
    print(err)

if db_connection:
    print(db_connection)
    print("SUCCESS")
    print("\n")

create = db_connection.cursor()

print("Enter Breeding Info")
k = input("Egg Group")
k=k.capitalize()
ka = input("% Male")
kb = input("% Female")
kc = input("Egg Cycle")

pokemonKey = None
create.execute("SELECT COUNT(p_PokeID) FROM Pokemon") #Genereates a Pokemon ID
pokemonKey = create.fetchone()[0]
pokemonKey += 1

egg = None
create.execute("SELECT eg_EggID FROM EggGroup WHERE eg_name = '" + k+ "';");
egg = create.fetchone()[0]


try:  # INSERTS VALUES IN Breeding TABLE
    create.execute("INSERT INTO Breeding VALUES(" + "'" + str(pokemonKey) + "'" + ", '" + str(egg)
                   + "','" + str(ka) + "','" + str(kb) + "','" + str(kc) + "'" + ");")
except sqlite3.Error as e:
    print(e)


create.execute("SELECT * FROM Breeding ")
st=create.fetchall()
for row in st:
 print(row)