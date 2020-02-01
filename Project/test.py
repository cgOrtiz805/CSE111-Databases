import sqlite3
from tkinter import *

def Insert_Mon_But():
    root= Tk()
    root.title("Inserting Pokemon")
    def namesearch():
        db_name = r"C:/Users/cortiz42/Documents/CSE111/Project/Pokedex.db"
        db_connection = sqlite3.connect(db_name)
        create = db_connection.cursor()

        # mon=e0.get()
        # mon=mon.capitalize()
        # height = e1.get()
        # weight = e2.get()
        # habitat = e3.get()
        # habitat = habitat.capitalize()
        # p_type = e4.get()
        # p_type = p_type.capitalize()
        # s_type = e5.get()
        # s_type = s_type.capitalize()
        # species = e6.get()
        # species = species.title()
        # ability=e7.get()
        # ability = ability.capitalize()
        # desc=e8.get()
        # hp=e9.get()
        # atk=e10.get()
        # defe=e11.get()
        # sp_atk = e12.get()
        # sp_def=e13.get()
        # speed=e14.get()
        egg = e15.get()
        egg = egg.title()
        male = e16.get()
        female = e17.get()
        cycle = e18.get()





        # e0.delete(0,END)
        # e1.delete(0,END)
        # e2.delete(0,END)
        # e3.delete(0,END)
        # e4.delete(0,END)
        # e5.delete(0,END)
        # e6.delete(0,END)
        # e7.delete(0,END)
        # e8.delete(0,END)
        # e9.delete(0,END)
        # e10.delete(0,END)
        # e11.delete(0,END)
        # e12.delete(0,END)
        # e13.delete(0,END)
        # e14.delete(0,END)
        e15.delete(0,END)
        e16.delete(0,END)
        e17.delete(0,END)
        e18.delete(0,END)

        pokemonKey = None
        create.execute("SELECT COUNT(p_PokeID) FROM Pokemon")  # Genereates a Pokemon ID
        pokemonKey = create.fetchone()[0]
        pokemonKey += 1
        print(pokemonKey)
        # print(mon)
        #
        # create.execute("SELECT h_HabitatID FROM Habitat WHERE h_name = '" + habitat + "';");  # Generates the Habitat ID
        # habitat = create.fetchall()[0]
        # print(str(habitat[0]))
        #
        # create.execute("SELECT pt_PtypeID FROM PrimaryType WHERE pt_type = '" + p_type + "';");  # Generates the PrimaryTypeID
        # p_type = create.fetchall()[0]
        # print(str(p_type[0]))
        #
        # create.execute( "SELECT st_StypeID FROM SecondaryType WHERE st_type = '" + s_type + "';");  # Generates the SecondaryTypeID
        # secondarytype = create.fetchall()[0]
        # print(str(secondarytype[0]))
        #
        # create.execute("SELECT s_SpeciesID FROM Species WHERE s_name = '" + species + "';");  # Generates the Species ID
        # species = create.fetchall()[0]
        # print(str(species[0]))
        #
        # create.execute("SELECT a_AbilityID FROM Ability WHERE a_name = '" + ability + "';")  # Generates the AbilityID
        # ability = create.fetchall()[0]
        # print(str(ability[0]))
        #
        # try:  # INSERTS VALUES INTO Pokemon Table
        #     create.execute("INSERT INTO Pokemon  VALUES(" + "'" + str(pokemonKey) + "'" + ", '" + mon + "','"  # Need to add input for secondary, speceis, ability and entry
        #                    + str(height) + "','" + str(weight) + "','" + str(habitat[0]) + "','" + str(p_type[0])
        #                    + "','" + str(secondarytype[0]) + "','" + str(species[0]) + "','" + str(ability[0]) + "','" + str(desc) + "'" + ");")
        #     db_connection.commit()
        # except sqlite3.Error as e:
        #     print(e)
        # try:  # INSERTS VALUES IN STATS TABLE
        #     create.execute("INSERT INTO Stats VALUES(" + "'" + str(pokemonKey) + "'" + ", '" + str(hp) + "','" + str(atk)
        #                    + "','" + str(defe) + "','" + str(sp_atk) + "','" + str(sp_def) + "','" + str(speed) + "'" + ");")
        #     db_connection.commit()
        # except sqlite3.Error as e:
        #     print(e)


        create.execute("SELECT eg_EggID FROM EggGroup WHERE eg_name = '" + egg + "';");
        egg = create.fetchone()[0]
        print(str(egg))
        print(type(egg))
        try:  # INSERTS VALUES IN Breeding TABLE
            create.execute("INSERT INTO Breeding VALUES(" + "'" + str(pokemonKey) + "'" + ", '" + str(egg)
                           + "','" + str(male) + "','" + str(female) + "','" + str(cycle) + "'" + ");")
            #db_connection.commit()
        except sqlite3.Error as e:
            print(e)








    # Label(root, text = "Pokemon Name").grid(row=0)
    # e0 = Entry(root)
    # e0.grid(row=0, column=1)
    #
    # Label(root,text = "Height").grid(row=1)
    # e1 = Entry(root)
    # e1.grid(row=1, column =1)
    #
    # Label(root, text="Weight").grid(row=2)
    # e2 = Entry(root)
    # e2.grid(row=2, column=1)
    #
    # Label(root, text="Habitat").grid(row=3)
    # e3 = Entry(root)
    # e3.grid(row=3,column = 1)
    #
    # Label(root, text="Primary Type").grid(row=4)
    # e4 = Entry(root)
    # e4.grid(row=4, column=1)
    #
    # Label(root, text="Secondary Type").grid(row=5)
    # e5 = Entry(root)
    # e5.grid(row=5, column=1)
    #
    # Label(root, text="Species").grid(row=6)
    # e6 = Entry(root)
    # e6.grid(row=6, column=1)
    #
    # Label(root, text="Ability").grid(row=7)
    # e7 = Entry(root)
    # e7.grid(row=7, column=1)
    #
    # Label(root, text="Description").grid(row=8)
    # e8 = Entry(root) #Width = 50
    # e8.grid(row=8, column=1)
    #
    # Label(root, text="HP").grid(row=9)
    # e9 = Entry(root)
    # e9.grid(row=9, column=1)
    #
    # Label(root, text="Attack").grid(row=10)
    # e10 = Entry(root)
    # e10.grid(row=10, column=1)
    #
    # Label(root, text="Defense").grid(row=11)
    # e11 = Entry(root)
    # e11.grid(row=11, column=1)
    #
    # Label(root, text="SP_Atk").grid(row=12)
    # e12 = Entry(root)
    # e12.grid(row=12, column=1)
    #
    # Label(root, text="SP_Def").grid(row=13)
    # e13 = Entry(root)
    # e13.grid(row=13, column=1)
    #
    # Label(root, text="Speed").grid(row=14)
    # e14 = Entry(root)
    # e14.grid(row=14, column=1)

    Label(root, text="Egg Group").grid(row=15)
    e15 = Entry(root)
    e15.grid(row=15, column=1)

    Label(root, text="Male").grid(row=16)
    e16 = Entry(root)
    e16.grid(row=16, column=1)

    Label(root, text="Female").grid(row=17)
    e17 = Entry(root)
    e17.grid(row=17, column=1)

    Label(root, text="Egg Cycle").grid(row=18)
    e18 = Entry(root)
    e18.grid(row=18, column=1)







    submit = Button(root, text = "Submit", command = namesearch)
    submit.grid(row=19, columnspan=2, pady=10, padx=10, ipadx=100)
    root.mainloop()
Insert_Mon_But()
