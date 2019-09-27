"""
Markbook Application
Group members: Marcus Tuen Muk, Liu Chen Wu, Stella Hong
"""
from typing import Dict
import json


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    print ("""OPTIONS
    1: Create
    2: Delete
    3: Edit
    4: Return to menu""")

    a = int(input("What would you like to do? "))

    if a == 1:
        name = input("What is the name of the assignment? ")
        due = input("When is the due date? ")
        points = int(input("How much is this assignment worth. "))

        assigment1 = {
            "name": name,
            "due": due,
            "points": points
        }
    
    elif a == 2:
        to_be_deleted = input("Which assignment would you like to delete?")

        


    elif a == 3:
        pass
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
    with open("classroom.json", 'w') as f:
        json.dump(classroom)
    return classroom


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""

    return 0

def add_student_to_classroom(student: str, classroom: dict):

    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """

    classroom["students"] = student

    return classroom
    pass


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    pass


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    pass
