students = []
courses = []

def input_no_of_student():
    return int(input('Enter number of student'))

# Ask the user to enter a list of info for an type
def input_infos():
    name = input('Enter student name:')
    dob = input('Enter student date of birth:')
    id = input ('Enter student id:')
    course = input('Enter student course name:')

    return {'id':id, 'name':name, 'dob':dob, 'course':course}

# Input the student mark in a course base on the course id
def input_mark(course):
    for student in students:
        mark = float(input(f"enter marks for student {student['id']} in course {course}:"))
    return mark
    # TODO: check mark in student or not
    # If not, enter the mark for the course


# Display a list of students
def list_students(students):

    # TODO: check what happens if there's no student (hint: len(students))
    print("There aren't any students yet")

    # TODO: display the student list
    print("Here is the student list: ")

    # TODO: add loop function to check the info of student
    for student in students:
        print(f"Student ID: {student['id']}, name: {student['name']}, date of birth: {student['DoB']}")

    # TODO: check if mark student and print out the information
    if "marks" in student:
        print("Marks (Course Id - Mark): ", end="")   

# Display a list of courses
def list_courses(courses):
    # TODO: check what happens if there's no course (hint: len(course))
    print("There aren't any courses yet")
        
    print("Here is the course list: ")
    for course in courses:
        print(f"course:{course['name']}")

# Main function for the "game"
def main():
    # Initialize the list for DATA option
    courses = []
    students = []
    num_students = 0
    num_courses = 0

    while(True):
        print("""
    0. Exit
    1. 
    2. 
    ...
    n
    """)
        option = int(input("Your choice: "))                                                         # Choose option from 0 -> n
        if option == 0:
            break

        elif option == 1:                                                                            # Option 1
            input_something(student)
        elif option == 2:                                                                            # Option 2                                                     
            input_infos(course)

# Call the main function
if __name__ == "__main__":
    main()
