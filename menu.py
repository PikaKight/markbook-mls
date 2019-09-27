
from markbook import *

def student():

   
    while True:

        

        ask = int(input("Press 1 to go back: "))

        if ask == 1:
            break
        else:
            continue

    menu()

def classroom():
    
    while True:

        print ("hello")

        ask = int(input("Press 1 to go back: "))


        if ask == 1:
            break
        else:
            continue

    menu()

def assignment():

    while True:
        create_assignment()

    menu()

def markbook():
  
    while True:

        print ("hello")

        ask = int(input("Press 1 to go back: "))

        if ask == 1:
            break
        else:
            continue

    menu()

def menu():

    print ("""
        1: Student
        2: Classroom
        3: Assignments
        4: Markbook
        5: Quit
    """)
    
    a = int(input("What would you like do: "))

    if a == 1:
        student()
    elif a == 2:
        classroom()
    elif a == 3:
        assignment()
    elif a == 4:
        markbook()
    elif a == 5:
        q =int(input("Are you sure you want to quit (1/2):"))
        if q == 1:
            quit
        else:
            menu()

menu()