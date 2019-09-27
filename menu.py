
from markbook import *

def student():

   
    while True:
        
        print ("""
        OPTIONS
        1: Add
        2: Delete
        3: Edit
        4: Return to menu
        """)
        
        ask = int(input("What you you like to do: "))
        
        
        if ask == 1:
             add_student_to_classroom()  

        elif ask == 2:
            to_be_deleted = input("Which student would you like to delete: ")

        elif ask == 3:
            pass

        elif ask == 4:
            break
        else:
            print ("Not a valid response. Please try again.")
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
        
        
        if ask == 1:
            course_code = input ("What is the course code:")
            
            course_name = input ("What is the course name:")

            period = input ("What period is the course in:")

            teacher = input("Who is the teacher:")

            create_classroom(course_code,course_name, period, teacher)    

        elif ask == 2:
            to_be_deleted = input("Which classroom would you like to delete?")
        elif ask == 3:
            pass
        elif ask == 4:
            break
        else:
            print ("Not a valid response. Please try again.")
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
        
        if ask == 1:
            create_assignment()    
        elif ask == 2:
            to_be_deleted = input("Which assignment would you like to delete?")
        elif ask == 3:
            pass
        elif ask == 4:
            break
        else:
            print ("Not a valid response. Please try again.")
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
        
       
        if ask == 1:
            create_assignment()    
        elif ask == 2:
            to_be_deleted = input("Which assignment would you like to delete?")
        elif ask == 3:
            pass
        elif ask == 4:
            break
        else:
            print ("Not a valid response. Please try again.")
            

    menu()

def menu():

    print ("""
        1: Student
        2: Classroom
        3: Assignments
        4: Markbook
        5: Quit
    """)
    
    ask = int(input("What would you like do: "))

    if ask == 1:
        student()

    elif ask == 2:
        classroom()

    elif ask == 3:
        assignment()

    elif ask == 4:
        markbook()

    elif ask == 5:
        q = input("Are you sure you want to quit (y/n):")
        
        if q == "y":
            quit()
        else:
            menu()

menu()