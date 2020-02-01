import time
import sqlite3

def main():
    db_name = r"C:/Users/cortiz42/Documents/CSE111/Project/Pokedex.db"
    db_connection = create_connection(db_name)
    menu(db_connection)

def create_connection(db_connection): #Connects to DataBase
    db_connection = None
    db_name = r"C:/Users/cortiz42/Documents/CSE111/Project/Pokedex.db"
    try:
        db_connection = sqlite3.connect(db_name)
    except sqlite3.Error as err:
        print(err)


    if db_connection:
     print(db_connection)
     print("Connected to Pokedex")
     print("\n")
    return db_connection

def menu(db_connection):
    while True:
        choice = input("""
                             1:View Tables
                             2:Search Pokemon
                             3:Insert Pokemon
                             4:Delete Pokemon
                             5:End


                             Please enter your choice: """)
        if choice == '1':
            choice1 = input("""
                             1: View Pokedex
                             2: View Ability
                             3: View Habitat
                             4: View PrimaryType
                             5: View Species
                             6: View Breeding
                             7: View EggGroup
                             8: View Stats


                             Please enter your choice: """)
            if choice1 == '1':
                view_pokemon(db_connection)


            if choice1 == '2':
                view_ability(db_connection)

            if choice1 == '3':
                view_habitat(db_connection)

            if choice1 == '4':
                view_primaryType(db_connection)

            if choice1 == '5':
                view_species(db_connection)

            if choice1 == '6':
                view_breeding(db_connection)

            if choice1 == '7':
                view_eggGroup(db_connection)

            if choice1 == '8':
                view_stats(db_connection)


        if choice == '2':
            choice2 = input("""
                             1: Search by a Pokemon by Name
                             2: Search pokemon by Type
                             3: Search pokemon by Ability
                             4: Search pokemon by Habitat
                             5: Search pokemon by eggGroup
                             6: Search pokemon Evolution



                             Please enter your choice: """)
            if choice2 == '1':
                Search_Pokemon(db_connection)

            if choice2 == '2':
                Search_byType(db_connection)

            if choice2 == '3':
                Search_byAbility(db_connection)

            if choice2 == '4':
                Search_byHabitat(db_connection)

            if choice2 == '5':
                Search_byEggGroup(db_connection)

            if choice2 == '6':
                Search_byEvolution(db_connection)


        if choice == '3':
            choice3 = input("""
                             1: Input a Pokemon
                             2: Input a ability
                             3: Input a species


                             Please enter your choice: """)
            if choice3 == '1':
                Insert_Mon(db_connection)

            if choice3 == '2':
                insert_ability(db_connection)

            if choice3 == '3':
                insert_species(db_connection)


        if choice == '4':
            choice4 = input("""
                             1: Delete a pokemon
                             2: Delete a ability
                             3: Delete a species

                             Please enter your choice: """)
            if choice4 == '1':
                delete_pokemon(db_connection)

            if choice4 == '2':
                delete_ability(db_connection)

            if choice4 == '3':
                delete_species(db_connection)


        if choice == '5':
            try:

                if db_connection != None:
                    db_connection.close()
                    print("Data Base disconnected")
                    print("Ending Program")
                    time.sleep(2)
                    break
            except sqlite3.Error as Err:
                print(Err)



def view_pokemon(db_connection):    #Fetches all information from every applicable table for all pokemon
    try:
        create = db_connection.cursor()
        create.execute("SELECT * FROM (SELECT p_PokeID,p_name, height, weight,h_name,"
                       " pt_type, st_type, s_name,a_name, eg_name,HP,Attack, Defense, SP_Atk,SP_Def, Speed, Male, Female, Egg_cycle "
                       "FROM Pokemon INNER JOIN PrimaryType ON pt_PtypeID = p_PtypeID "
                       "INNER JOIN SecondaryType ON p_StypeID = st_StypeID "
                       "INNER JOIN Species ON p_SpeciesID = s_SpeciesID "
                       "INNER JOIN Ability ON p_AbilityID = a_AbilityID "
                       "INNER JOIN Habitat ON h_HabitatID = p_HabitatID "
                       "INNER JOIN Breeding ON p_PokeID=b_PokeID "
                       "INNER JOIN EggGroup ON b_EggID = eg_EggID "
                       "INNER JOIN Stats ON p_PokeID = sts_PokeID) ;")
        mons = create.fetchall()
        print("ID" + "\t\t" + " Name" + "\t\t" + "Height(ft)" + "\t" + "Weight(lbs)" + "\t" + " Habitat" + "\t" + "PrimaryType" + "\t" + "SecondaryType" + "\t" + "Species" + "\t\t" + "Ability" + "\t\t\t" +  "Egg" + "\t\t"+ "HP" + "\t" + "Atk" + "\t" + "Def" + "\t" + "Sp_Atk" + "\t" + "Sp_Def" + "\t" + "Spd" + "\t" + "Male" + "\t" + "Female" + "\t" + "Cycle")
        for row in mons:
            print("{: >3} {: >13} {: >10}{: >10} {: >15} {: >10}{: >10} {: >12} {: >15}{: >13} {: >5} {: >3}{: >3}{: >6} {: >8} {: >5}{: >6} {: >6}{: >6}".format(*row))
        # print(
        #     "ID" + "\t\t" + " Name" + "\t\t" + "Height(ft)" + "\t\t" + "Weight(lbs)" + "\t\t" + " Habitat" + "\t\t" + "PrimaryType" + "\t\t" + "SecondaryType" + "\t\t" + "Species" + "\t\t" + "Ability" + "\t" +  "Egg" + "\t"+ "HP" + "\t" + "Attack" + "\t" + "Defense" + "\t" + "SPAttack" + "\t" + "Speed" + "\t" + "Male" + "\t" + "Female" + "\t" + "Egg Cycle")
        # for q in mons:
        #     # print(q)
        #     print(str(q[0]) + "\t\t" + str(q[1]) + "\t\t" + str(int(q[2])) + "\t\t\t" +str(q[3]) + "\t\t" + str(
        #         q[4]) + "\t\t" + str(q[5]) + "\t\t" + str(q[6]) + "\t\t" + str(q[7]) +"\t\t" + str(
        #         q[8]) + "\t\t" + str(q[9]) + "\t\t" + str(q[10]) + "\t\t" + str(
        #         q[11]) + "\t\t" + str(
        #         q[12]) + "\t\t" + str(q[13]) + "\t\t" + str(q[14]) + "\t\t" + str(
        #         q[15]) + "\t\t" + str(
        #         q[16]) + "\t\t" + str(q[17]))

    except sqlite3.Error as e:
        print(e)
    create.close()
def Insert_Mon(db_connection):
    create = db_connection.cursor()
    print("Enter General Information")
    a = input("Name: ")
    a=a.capitalize()
    b = input("Height: ")
    c = input("Weight: ")
    d = input("Habitat: ")
    d=d.capitalize()
    e = input("Primary Type: ")
    e=e.capitalize()
    f = input("Secondary Type: ")
    f=f.capitalize()
    g = input("Species: ")
    g=g.title()
    h = input("Ability: ")
    h=h.capitalize()
    i=input("Descrpition: ")
    print("Enter the Stats")
    j=input("HP: ")
    ja=input("Attack: ")
    jb=input("Defense: ")
    jc = input("SP_Atk: ")
    jd = input("SP_Def: ")
    je = input("Speed: ")
    k = input("Egg Group: ")
    k=k.capitalize()
    ka= input("% Male: ")
    kb = input("% Female" )
    kc = input("Egg Cycle: ")

    pokemonKey = None
    create.execute("SELECT COUNT(p_PokeID) FROM Pokemon") #Genereates a Pokemon ID
    pokemonKey = create.fetchone()[0]
    pokemonKey += 1

    create.execute("SELECT h_HabitatID FROM Habitat WHERE h_name = '" + d + "';"); # Generates the Habitat ID
    habitat = create.fetchall()[0]
    #print(str(habitat[0]))

    create.execute("SELECT pt_PtypeID FROM PrimaryType WHERE pt_type = '" + e + "';"); #Generates the PrimaryTypeID
    primarytype = create.fetchall()[0]

    create.execute("SELECT st_StypeID FROM SecondaryType WHERE st_type = '"+ f + "';"); #Generates the SecondaryTypeID
    secondarytype = create.fetchall()[0]

    create.execute("SELECT s_SpeciesID FROM Species WHERE s_name = '"+ g +"';"); #Generates the Species ID
    species = create.fetchall()[0]

    create.execute("SELECT a_AbilityID FROM Ability WHERE a_name = '"+ h+ "';") #Generates the AbilityID
    ability = create.fetchall()[0]


    try:  # INSERTS VALUES INTO Pokemon Table
        create.execute("INSERT INTO Pokemon  VALUES(" + "'" + str(pokemonKey) + "'" + ", '" + a + "','" #Need to add input for secondary, speceis, ability and entry
                       + str(b) + "','" + str(c) + "','" + str(habitat[0]) + "','" + str(primarytype[0]) + "','" + str(secondarytype[0])+ "','" + str(species[0])+"','" + str(ability[0]) +"','" +str(i)+ "'" + ");")
        db_connection.commit()
    except sqlite3.Error as e:
        print(e)
    try: #INSERTS VALUES IN STATS TABLE
        create.execute("INSERT INTO Stats VALUES(" + "'" + str(pokemonKey) + "'" + ", '" + str(j)+ "','"+str(ja) + "','" + str(jb)+ "','" + str(jc)+"','" + str(jd) +"','" +str(je)+ "'" + ");")
        db_connection.commit()
    except sqlite3.Error as e:
        print(e)

    egg = None
    create.execute("SELECT eg_EggID FROM EggGroup WHERE eg_name = '" + k + "';");
    egg = create.fetchone()[0]
    try:  # INSERTS VALUES IN Breeding TABLE
        create.execute("INSERT INTO Breeding VALUES(" + "'" + str(pokemonKey) + "'" + ", '" + str(egg)
                       + "','" + str(ka) + "','" + str(kb) + "','" + str(kc) + "'" + ");")
        db_connection.commit()
    except sqlite3.Error as e:
        print(e)


def Search_Pokemon(db_connection): #Basiclly the same as view pokemon, but takes in a input pokemon name which then prints out all the information for that pokemon
    create = db_connection.cursor()
    mon = input("Enter a Pokemon Name: ")
    mon=mon.capitalize()
    try:
        create.execute("SELECT * FROM (SELECT p_PokeID,p_name, height, weight,h_name,"
                       " pt_type, st_type, s_name,a_name, eg_name,HP,Attack, Defense, SP_Atk,SP_Def, Speed, Male, Female, Egg_cycle "
                       "FROM Pokemon INNER JOIN PrimaryType ON pt_PtypeID = p_PtypeID "
                       "INNER JOIN SecondaryType ON p_StypeID = st_StypeID "
                       "INNER JOIN Species ON p_SpeciesID = s_SpeciesID "
                       "INNER JOIN Ability ON p_AbilityID = a_AbilityID "
                       "INNER JOIN Habitat ON h_HabitatID = p_HabitatID "
                       "INNER JOIN Breeding ON p_PokeID=b_PokeID "
                       "INNER JOIN EggGroup ON b_EggID = eg_EggID "
                       "INNER JOIN Stats ON p_PokeID = sts_PokeID WHERE p_name = '" + mon+"') ;")

        pokemon = create.fetchall()
        print(
            "ID" + "\t\t" + " Name" + "\t\t" + "Height(ft)" + "\t" + "Weight(lbs)" + "\t" + " Habitat" + "\t" + "PrimaryType" + "\t" + "SecondaryType" + "\t" + "Species" + "\t\t" + "Ability" + "\t\t\t" + "Egg" + "\t\t" + "HP" + "\t" + "Atk" + "\t" + "Def" + "\t" + "Sp_Atk" + "\t" + "Sp_Def" + "\t" + "Spd" + "\t" + "Male" + "\t" + "Female" + "\t" + "Cycle")
        for row in pokemon:
            print(
                "{: >3} {: >13} {: >10}{: >10} {: >15} {: >10}{: >10} {: >12} {: >15}{: >13} {: >5} {: >3}{: >3}{: >6} {: >8} {: >5}{: >6} {: >6}{: >6}".format(*row))
    except sqlite3.Error as e:
        print(e)


def Search_byType(db_connection):  # Same as view pokemon but takes in a input type that returns all pokemon that have that as a primary and or secondary type.
    create = db_connection.cursor()
    pt_type = input(" 1st type:  ")
    pt_type = pt_type.capitalize()
    st_type = input(" 2nd type, otherwise put 'x' for single type:  ")
    st_type = st_type.capitalize()
    query = "SELECT * FROM (SELECT p_name,pt_type,st_type FROM Pokemon INNER JOIN PrimaryType ON pt_PtypeID = p_PtypeID INNER JOIN SecondaryType ON p_StypeID = st_StypeID  WHERE pt_type = ? AND st_type = ?) "
    create.execute(query, [pt_type,st_type])
    mons = create.fetchall()
    print(
        "Name" + "\t\t" + "Primary Type" + "\t\t" + "Secondary Type")
    for row in mons:
        print(
            "{: >3}{: >15}{: >15}".format(*row))


def Search_byAbility(db_connection):
    create = db_connection.cursor()
    a_name = input("Enter a Ability:  ")
    a_name = a_name.title()
    query = " SELECT p_name, a_name FROM Pokemon INNER JOIN Ability ON p_AbilityID = a_AbilityID WHERE a_name = ? "
    create.execute(query, [a_name])
    mons = create.fetchall()
    print(" Name" + " " + "   " + " ""Ability" + " ")
    for row in mons:
        print(
            "{: >3}{: >12}".format(*row))
        #print(str(row[0]) + "   " + str(row[1]))

def Search_byHabitat(db_connection):
    create = db_connection.cursor()
    h_name = input("Enter a Habitat: ")
    h_name = h_name.title()
    query = " SELECT p_name, h_name FROM Pokemon INNER JOIN Habitat ON h_HabitatID = p_HabitatID WHERE h_name = ? "
    create.execute(query, [h_name])
    mons = create.fetchall()
    print(" Name" + " " + "   " + "   " + "   " + " ""Habitat" + " ")
    for row in mons:
        print("   " + str(row[0]) + "   " + "   " + str(row[1]))

def Search_byEggGroup(db_connection):
    create = db_connection.cursor()
    eg_name = input("Enter a egg Group: ")
    eg_name = eg_name.title()
    query = " SELECT p_name, eg_name FROM Pokemon INNER JOIN EggGroup ON b_EggID = eg_EggID INNER JOIN Breeding ON p_PokeID = b_PokeID WHERE eg_name = ? "
    create.execute(query, [eg_name])
    mons = create.fetchall()
    print(" Name" + " " + "   " + "   " + "   " + " ""Egg Group" + " ")
    for row in mons:
        print("   " + str(row[0]) + "   " + "   " + str(row[1]))


def Search_byEvolution(db_connection):
    create = db_connection.cursor()
    p_name = input("Enter a Pokemon:  ")
    p_name = p_name.capitalize()
    query = "SELECT p_name,e_name, co_condition, Item, level FROM Pokemon INNER JOIN Evolve ON p_PokeID = e_PokeID INNER JOIN Condition ON co_ConditionID = e_ConditionID WHERE p_name = ?"
    create.execute(query, [p_name])
    mons = create.fetchall()
    print("  Name" + "   " + " ""Evolution" + "     " + " ""Condition" + "    " + " ""Item" + "    " + "Level#")
    for row in mons:
        print("   " + str(row[0]) + "   " + str(row[1]) + "   " + "   " + str(row[2]) + "   " + "   " + str(
            row[3]) + "   " + "   " + str(row[4]))

def view_ability(db_connection):
    create = db_connection.cursor()
    try:
        create.execute("SELECT * FROM Ability ")
        mons = create.fetchall()
        print(
            " ID " + " " + " Name " + " " + "   " + "   " + "   " + " Entry " + " ")
        for row in mons:
            print(str(row[0]) + "   " + str(row[1]) + "   " + "   " + "   " + str(row[2]))
    except sqlite3.Error as e:
        print(e)

def view_habitat(db_connection):
    create = db_connection.cursor()
    create.execute("SELECT * FROM Habitat ")
    mons = create.fetchall()
    print(
        " ID " + " " + " Name " + " " + "   " + "   " + "   " + " Entry " + " ")
    for row in mons:
        print(str(row[0]) + "   " + str(row[1]) + "   " + "   " + "   " + str(row[2]))

def view_primaryType(db_connection):
    create = db_connection.cursor()
    create.execute("SELECT * FROM PrimaryType ")
    mons = create.fetchall()
    print(
        " ID " + " " + " Name Type " + " ")
    for row in mons:
        print("   " + str(row[0]) + "   " + str(row[1]))

def view_species(db_connection):
    create = db_connection.cursor()
    create.execute("SELECT * FROM Species ")
    mons = create.fetchall()
    print(
        " ID " + " " + " Name " + " ")
    for row in mons:
        print("   " + str(row[0]) + "   " + str(row[1]))

def view_breeding(db_connection):
    create = db_connection.cursor()
    create.execute("SELECT * FROM Breeding ")
    mons = create.fetchall()
    print(
        " Poke ID " + " " + " Egg ID " + " " + " Male " + " " + " Female " + " " + " Egg Cycle " + " ")
    for row in mons:
        print("   " + str(row[0]) + "   " + "   " + str(row[1]) + "   " + "   " + "   " + str(
            row[2]) + "   " + "   " + str(row[3]) + "   " + "   " + str(row[4]))

def view_eggGroup(db_connection):
    create = db_connection.cursor()
    create.execute("SELECT * FROM EggGroup ")
    mons = create.fetchall()
    print(
        " ID " + " " + " Name " + " ")
    for row in mons:
        print("   " + str(row[0]) + "   " + str(row[1]))


def view_stats(db_connection):
    create = db_connection.cursor()
    create.execute("SELECT * FROM Stats ")
    mons = create.fetchall()
    print(
        " Poke ID" + " " + " HP " + " " + " Attack " + " " + " Defense " + " " + " Sp Atk " + " " + " Sp Def " + " " + " Speed " + " ")
    for row in mons:
        print("   " + str(row[0]) + "   " + "   " + str(row[1]) + "  " + "   " + str(row[2]) + "     " + "   " + str(
            row[3]) + "   " + "   " + str(
            row[4]) + "   " + "   " + str(row[5]) + "  " + "   " + "   " + str(row[6]))


def insert_ability(db_connection):
    create = db_connection.cursor()
    print("Enter Ability Information")
    a = input("Name: ")
    a = a.title()
    b = input("Description: ")


    create.execute("SELECT COUNT(a_AbilityID) FROM Ability")  # Genereates a Pokemon ID
    abilityKey = create.fetchone()[0]
    abilityKey += 1

    try:  # INSERTS VALUES IN ability TABLE
        create.execute("INSERT INTO Ability VALUES(" + "'" + str(abilityKey) + "'" + ", '" + str(a)
                       + "','" + str(b)  + "'" + ");")
        db_connection.commit()
    except sqlite3.Error as e:
        print(e)

def insert_species(db_connection):
    create = db_connection.cursor()
    print("Enter Species Info")
    a = input("Name: ")
    a=a.title()
    create.execute("SELECT COUNT(s_SpeciesID) FROM Species")  # Genereates a Pokemon ID
    speciesKey = create.fetchone()[0]
    speciesKey += 1
    try:  # INSERTS VALUES IN species TABLE
        create.execute("INSERT INTO Species VALUES(" + "'" + str(speciesKey) + "'" + ", '" + str(a)+ "'" + ");")
        db_connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_pokemon(db_connection):
    create = db_connection.cursor()

    a = input("Enter a pokemon you want to Delete: ")
    a = a.title()
    create.execute("SELECT p_PokeID FROM Pokemon WHERE p_name = '" + str(a) + "';"); #FINDS THE POKEMON ID
    ID = create.fetchone()[0]
    try:
     create.execute("DELETE FROM Pokemon WHERE p_PokeID = '" + str(ID) + "';"); #DELELTES FROM Pokemon
     db_connection.commit()
    except sqlite3.Error as e:
        print(e)

    try:
     create.execute("DELETE FROM Stats WHERE sts_PokeID = '" + str(ID) + "';"); #DELETES FROM STATS
     db_connection.commit()
    except sqlite3.Error as e:
       print(e)

    try:
     create.execute("DELETE FROM Breeding WHERE b_PokeID = '" + str(ID) + "';"); #DELETES FROM BREEDING
     db_connection.commit()
    except sqlite3.Error as e:
     print(e)
    print(a+" Successfully Deleted from all tables")



def delete_species(db_connection):
    create = db_connection.cursor()
    a=input("Enter a species you want to delete: ")
    a=a.title()
    try:
        create.execute("DELETE FROM Species WHERE s_name = '" + a + "';");
        db_connection.commit()
        print(a + " Successfully Deleted")
    except sqlite3.Error as e:
        print(e)


def delete_ability(db_connection):
    create = db_connection.cursor()
    a=input("Enter a Ability you want to delete: ")
    a=a.title()
    try:
        create.execute("DELETE FROM Ability WHERE a_name = '" + a + "';");
        db_connection.commit()
        print(a+ " Succesfully Deleted")
    except sqlite3.Error as e:
        print(e)




main()