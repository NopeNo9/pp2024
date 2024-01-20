class student:
    def input_no_of_student():
        return int(input('Enter number of students: '))

    def input_infos():
        name = input('Enter student name: ')
        dob = input('Enter student date of birth: ')
        id = input('Enter student ID: ')
        return {'id': id, 'name': name, 'dob': dob}

class course:
    def input_number_of_courses():
        return int(input('Enter the number of courses: '))

    def input_course_info():
        course_id = input('Enter course ID: ')
        course_name = input('Enter course name: ')
        return {'id': course_id, 'name': course_name}

class mark:
    def input_mark(course, students):
        marks = {}
        print(f"Enter marks for course: {course['name']}")
        for student in students:
            mark = float(input(f"Enter mark for student {student['name']} ({student['id']}): "))
            marks[student['id']] = mark
        return marks

class show_info:
    def list_students(students):
        print('Students:')
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

    def list_courses(courses):
        print('Courses:')
        for course in courses:
            print(f"ID: {course['id']}, Name: {course['name']}")

    def show_student_marks(course, marks):
        print(f"Marks for course: {course['name']}")
        for student_id, mark in marks.items():
            print(f"Student ID: {student_id}, Mark: {mark}")

def main():
    students = []
    courses = []

    num_students = student.input_no_of_student()
    for _ in range(num_students):
        student_info = student.input_infos()
        students.append(student_info)

    num_courses = course.input_number_of_courses()
    for _ in range(num_courses):
        course_info = course.input_course_info()
        courses.append(course_info)

    show_info.list_courses(courses)
    show_info.list_students(students)

    selected_course_id = input("Enter the ID of the course to input marks for: ")
    selected_course = None
    for course in courses:
        if course['id'] == selected_course_id:
            selected_course = course
            break

    if selected_course:
        marks = mark.input_mark(selected_course, students)
        show_info.show_student_marks(selected_course, marks)
    else:
        print("Invalid course ID.")

if __name__ == "__main__":
    main()