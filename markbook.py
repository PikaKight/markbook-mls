"""
Markbook Application
Group members: Marcus Tuen Muk, Liu Chen Wu, Stella Hong
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """

    assignment_list = []
    print(assignment_list)

    print("""OPTIONS
    1: Create
    2: Delete
    3: Edit
    4: Return to menu""")

    a = int(input("What would you like to do? "))


    if a == 1:
        name = input("What is the name of the assignment? ")
        due = input("When is the due date? ")
        points = int(input("How much is this assignment worth? "))


        assigment = {
            "name": name,
            "due": due,
            "points": points
        }

        assignment_list.append(assignment)

    elif a == 2:
        to_be_deleted = input("Enter the assignment to be deleted: ")

        for assignment in assignment_list:
            if assignment["name"] == to_be_deleted:
                assignment.clear()


    elif a == 3:
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


    elif a == 4:
        menu()


    return {}

def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    classroom = {
        "course_code": course_code,
        "course_name": course_name,
        "Period": period,
        "Teacher": teacher 
    }

    return classroom


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    return 0

def add_student_to_classroom(student, classroom):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """

    classroom["students"] = student

    return classroom
    pass
