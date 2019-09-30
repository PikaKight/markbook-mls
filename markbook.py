"""
Markbook Application
Group members: Marcus Tuen Muk, Liu Chen Wu, Stella Hong
"""
from typing import Dict
# from menu import *
import json

def create_assignment() -> Dict:  #name: str, due: str, points: int):
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """

    name = input("What is the name of the assignment? ")
    due = input("When is the due date? ")
    points = int(input("How much is this assignment worth. "))

    assigment1 = {
        "name": name,
        "due": due,
        "points": points
    }

    return {}


def delete_assignment():
    to_be_deleted = input("Which assignment would you like to delete? ")

    for assignment in assignment_list:
        if assignment["name"] == to_be_deleted:
            assignment.clear()


def edit_assignment():
    to_be_edited = input("Enter the assignment to be edited: ")

    for assignment in assignment_list:
        if assignment["name"] == to_be_edited:
            print("""What will you change?
            1: Name
            2: Due Date
            3: Points""")

            x = int(input())

            if x == 1:
                assignment["name"] = input("Enter the new name: ")
            elif x == 2:
                assignment["due"] = input("Enter the new due date: ")
            elif x == 3:
                assignment["points"] = int(input("Enter the new points: "))


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    with open ("classroom.json", 'r') as f:

        course = json.load(f)

    course[course_code] = { 
        "course_code": course_code,
        "course_name": course_name,
        "Period": period,
        "Teacher": teacher, 
        "Student": {}
        }

    with open("classroom.json", 'w') as f:
        json.dump(course,f)
    
     
    return course[course_code]

def delete_classroom(course_code:str) -> Dict:
    with open ("classroom.json", 'r') as f:
        course = json.load(f)

    try:
        del course[course_code]
    except KeyError:
        print("Course {} not found".format(course))
    
    with open("classroom.json", 'w') as f:
        json.dump(course,f)

    return course

def edit_classroom(course_code:str) -> Dict:
    while True:
        with open ("classroom.json", 'r') as f:
            course = json.load(f)

        print(
            """
            1: Course Code
            2: Course Name
            3: Period
            4: Teacher Name
            5: Return to Course OPTIONS
            """
        )
        
        ask = int(input("what would you like to change:"))

        if ask is 1:
            new_course_code = input("Please enter the new Course Code:")
            course[course_code]["course_code"] = new_course_code
            with open("classroom.json", 'w') as f:
                json.dump(course,f)
            
            cont = input("would you like to do more edits for this course (y/n):")
            
            if cont == "y":
                continue
            else:
                break

        elif ask == 2:
            new_course_name = input("Please enter the new Course Name:")
            course[course_code]["course_name"] = new_course_name
            with open("classroom.json", 'w') as f:
                json.dump(course,f)
            
            cont = input("would you like to do more edits for this course (y/n):")
            
            if cont == "y":
                continue
            else:
                break

        elif ask == 3:
            new_period = input("Please enter the new Period:")
            course[course_code]["Period"] = new_period
            with open("classroom.json", 'w') as f:
                json.dump(course,f)

            cont = input("would you like to do more edits for this course (y/n):")
            
            if cont == "y":
                continue
            else:
                break

        elif ask == 4:
            new_teacher = input("Please enter the new Teacher Name:")
            course[course_code]["Teacher"] = new_teacher
            with open("classroom.json", 'w') as f:
                json.dump(course,f)
            
            cont = input("would you like to do more edits for this course (y/n):")
            
            if cont == "y":
                continue
            else:
                break

        elif ask == 5:
            break
        
        else: 
            print("""

            This is an invalid option. Please try again.
            
            """)
def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    
    return 0

# def student_average():
    

def add_student_to_classroom(student: str):

    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    course_code = input("Which course is the {} in:".format(student))

    gender = input("Enter {}'s gender:".format(student))

    student_number = int(input("Enter {}'s student number:".format(student)))

    email = input("Enter {}'s school email:".format(student))

    comments = input("Enter your comments:")

    with open("Classroom.json", "r") as f:
        course = json.load(f)

    course[course_code]["Students"] = {
        "Student Name": student,
        "Gender": gender,
        "Studet Number": student_number,
        "Student Email": email,
        "Comments": comments
    }

    with open("Classroom.json", "w") as f:
        json.dump(course, f)

    return course[course_code]
    
def remove_student_from_classroom(course_code: str, student: str):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    with open("Classroom.json", "r") as f:
        course = json.load(f)

    try:
        del course[course_code]["Student"][student]
    except KeyError:
        print("Student {} not found".format(course))
    
    with open("classroom.json", 'w') as f:
        json.dump(course,f)

    return course[course_code]["Student"]

def edit_student(course_code: str, student: str):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    while True:
        with open ("classroom.json", 'r') as f:
            course = json.load(f)

        print(
            """
            1: Student Name
            2: Gender
            3: Student Number
            4: Email
            5: Comments 
            7: Return to Student OPTIONS
            """
        )
        
        ask = int(input("what would you like to change:"))

        if ask is 1:
            new_student_name = input("Please enter the new Student Name:")
            course[course_code]["Student"][student]["Student Name"] = new_student_name
            with open("classroom.json", 'w') as f:
                json.dump(course,f)
            
            cont = input("would you like to do more edits for this Student (y/n):")
            
            if cont == "y":
                continue
            else:
                break

        elif ask == 2:
            new_course_name = input("Please enter the new Course Name:")
            course[course_code]["course_name"] = new_course_name
            with open("classroom.json", 'w') as f:
                json.dump(course,f)
            
            cont = input("would you like to do more edits for this Student (y/n):")
            
            if cont == "y":
                continue
            else:
                break

        elif ask == 3:
            new_period = input("Please enter the new Period:")
            course[course_code]["Period"] = new_period
            with open("classroom.json", 'w') as f:
                json.dump(course,f)

            cont = input("would you like to do more edits for this Student (y/n):")
            
            if cont == "y":
                continue
            else:
                break

        elif ask == 4:
            new_teacher = input("Please enter the new Teacher Name:")
            course[course_code]["Teacher"] = new_teacher
            with open("classroom.json", 'w') as f:
                json.dump(course,f)
            
            cont = input("would you like to do more edits for this Student (y/n):")
            
            if cont == "y":
                continue
            else:
                break

        elif ask == 6:
            break
        else: 
            print("""

            This is an invalid option. Please try again.

            """)

    
    pass
