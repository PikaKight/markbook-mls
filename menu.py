def student():
    on = True
    while on:
        print ("hello")
        ask = input("Do you want to continue (Y/N): ")
        if ask == "N":
            on = False
        else:
            continue
    menu()

def classroom():
    on = True
    while on:
        print ("hello")
        ask = input("Do you want to continue (Y/N): ")
        if ask == "N":
            on = False
        else:
            continue
    menu()

def assignment():
    on = True
    while on:
        print ("hello")
        ask = input("Do you want to continue (Y/N): ")
        if ask == "N":
            on = False
        else:
            continue
    menu()

def markbook():
    on = True
    while on:
        print ("hello")
        ask = input("Do you want to continue (Y/N): ")
        if ask == "N":
            on = False
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
        q = input("Are you sure (Y/N):")
        if q == "Y":
            quit
        else:
            menu()

menu()