
from markbook import *

def student():

   
    while True:
        
        print ("""
        OPTIONS
        1: Create
        2: Delete
        3: Edit
        4: Return to menu
        """)
        
        ask = int(input("What you you like to do: "))
        
        if ask == 4:
            break
        else:
            continue

    menu()

def classroom():
    
    while True:

        print ("""
        OPTIONS
        1: Create
        2: Delete
        3: Edit
        4: Return to menu
        """)
        
        ask = int(input("What you you like to do: "))
        
        if ask == 4:
            break
        else:
            continue

    menu()

def assignment():

    while True:
        print ("""
        OPTIONS
        1: Create
        2: Delete
        3: Edit
        4: Return to menu
        """)
        
        ask = int(input("What you you like to do: "))
        
        if ask == 4:
            break
        else:
            continue

    menu()

def markbook():
  
    while True:

        print ("""
        OPTIONS
        1: Create
        2: Delete
        3: Edit
        4: Return to menu
        """)
        
        ask = int(input("What you you like to do: "))
        
        if ask == 4:
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