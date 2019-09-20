"""Creates an assignment represented as a dictionary

Args:
    name: the name of the assignment.
    due: the due date for the assignment.
    points: what the assignment is out of (denominator).
Returns:
    Assignment as a dictionary.
"""

assigment = {
    "name": "Assignment One",
    "due": "2019-10-02",
    "points": 40
}
assignment_list = [assignment]


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
    to_be_deleted = input("Which assignment would you like to delete? ")

    for assignment in assignment_list:
        if assignment["name"] == to_be_deleted:
            assignment.clear()
    
    


elif a == 3:
    print("Which assignment would you like to edit?")
    to_be_edited = input()

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

