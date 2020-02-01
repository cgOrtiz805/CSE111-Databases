from tkinter import *
# import tkMessageBox
import tkinter
import time
#
# root = tkinter.Tk()
#
# CheckFire = IntVar()
# CheckWater = IntVar()
# CheckFly = IntVar()
#
# def test():
#
#     # print(CheckVar1.get())
#     # print(CheckVar2.get()) # Notice the .get()
#     if CheckFire.get() ==1:
#         print("Yes fire")
#     if CheckWater.get() ==1:
#         print("Yes water")
#     if CheckFire.get() ==0:
#         print("No fire")
#     if CheckWater.get() ==0:
#         print("No water")
#     if CheckFly.get() ==1:
#         print("Yes Fly")
#     if CheckFly.get() ==0:
#         print("No Fly")
#
#
# fire = Checkbutton(root, text = "Fire", variable = CheckFire, command = test)
# water = Checkbutton(root, text = "Water", variable = CheckWater, command = test)
# flying = Checkbutton(root, text = "Flying", variable = CheckFly, command = test )
# fire.grid(row=1,columnspan=2, pady=10, padx=10, ipadx=100)
# water.grid(row=2,columnspan=2, pady=10, padx=10, ipadx=100)
# flying.grid(row=3,columnspan=2, pady=10, padx=10, ipadx=100)
# root.mainloop()


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
           #view_pokemon(db_connection)
            print("View Mon")

       if choice1 == '2':
           # #view_ability(db_connection)
            print("View Ability")
       if choice1 == '3':
           #view_habitat(db_connection)
           print("View Habitat")
       if choice1 == '4':
           #view_primaryType(db_connection)
           print("View Primarykey")
       if choice1 == '5':
           # view_species(db_connection)
           print("View Species")
       if choice1 == '6':
           #view_breeding(db_connection)
           print("View breeding")
       if choice1 == '7':
           #view_eggGroup(db_connection)
           print("View EggGroup")
       if choice1 == '8':
           #view_stats(db_connection)
           print("View Stats")



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
            #Search_Pokemon(db_connection)
            print("Search Name")
        if choice2 == '2':
            #Search_byType(db_connection)
            print("search type")
        if choice2 == '3':
            #Search_byAbility(db_connection)
            print("Search pokemon by Ability")
        if choice2 == '4':
            #Search_byHabitat(db_connection)
            print("Search pokemon by Habitat")
        if choice2 == '5':
            #Search_byEggGroup(db_connection)
            print("Search pokemon by eggGroup")
        if choice2 == '6':
            #Search_byEvolution(db_connection)
            print("Search pokemon Evolution")

    if choice == '3':
        choice3 = input("""
                         1: Input a Pokemon
                         2: Input a ability
                         3: Input a species
                         
                        
                         Please enter your choice: """)
        if choice3 == '1':
            #Insert_Mon(db_connection)
            print("Input a pokemon")
        if choice3 == '2':
            #insert_ability(db_connection)
            print("Input a Ability")
        if choice3 == '3':
            #insert_species(db_connection)
            print("Input a Species")


    if choice == '4':
        choice4 = input("""
                         1: Delete a pokemon
                         2: Delete a ability
                         3: Delete a species
                         
                         Please enter your choice: """)
        if choice4 == '1':
            # delete_pokemon(db_connection)
            print("Delete a pokemon")
        if choice4 == '2':
            #delete_ability(db_connection)
            print("Delete a Ability")
        if choice4 == '3':
            #delete_species(db_connection)
            print("Delete a Species")



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

