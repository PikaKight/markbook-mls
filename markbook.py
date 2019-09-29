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

    course[course_code] = { 
        "course_code": course_code,
        "course_name": course_name,
        "Period": period,
        "Teacher": teacher 
        }

    # classroom = {
    #     "course_code": course_code,
    #     "course_name": course_name,
    #     "Period": period,
    #     "Teacher": teacher 
    # } 

    with open("classroom.json", 'w') as f:
        json.dump(course,f)
    
     
    return course[course_code]


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    
    return 0


def add_student_to_classroom(student: str, classroom: dict):

    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """

    student_list = []

    student_list.append(student)

    couse["students"] = student_list

    return course
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
