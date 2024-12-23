# Global variables to store information
students = []
courses = []
marks = {}

# Input Functions
def input_number_of_students():
    """Input the number of students in the class."""
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        input_student_information()

def input_student_information():
    """Input student information: id, name, and DoB."""
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
    students.append({"id": student_id, "name": name, "dob": dob})

def input_number_of_courses():
    """Input the number of courses."""
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        input_course_information()

def input_course_information():
    """Input course information: id, name."""
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append({"id": course_id, "name": name})
    marks[course_id] = {}  # Initialize marks for the course

def input_marks_for_course():
    """Select a course and input marks for students in that course."""
    if not courses:
        print("No courses available. Please add courses first.")
        return
    
    print("Available courses:")
    list_courses()
    course_id = input("Enter the course ID to input marks: ")

    if course_id not in [course["id"] for course in courses]:
        print("Invalid course ID.")
        return

    print("Input marks for the selected course:")
    for student in students:
        student_id = student["id"]
        mark = float(input(f"Enter marks for {student['name']} (ID: {student_id}): "))
        marks[course_id][student_id] = mark

# Listing Functions
def list_courses():
    """List all courses."""
    if not courses:
        print("No courses available.")
    else:
        print("Courses:")
        for course in courses:
            print(f"ID: {course['id']}, Name: {course['name']}")

def list_students():
    """List all students."""
    if not students:
        print("No students available.")
    else:
        print("Students:")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def show_student_marks():
    """Show student marks for a given course."""
    if not courses:
        print("No courses available. Please add courses first.")
        return
    
    print("Available courses:")
    list_courses()
    course_id = input("Enter the course ID to view marks: ")

    if course_id not in marks:
        print("Invalid course ID.")
        return
    
    if not marks[course_id]:
        print("No marks available for this course.")
    else:
        print(f"Marks for course {course_id}:")
        for student_id, mark in marks[course_id].items():
            student_name = next(student["name"] for student in students if student["id"] == student_id)
            print(f"Student: {student_name} (ID: {student_id}), Mark: {mark}")

# Main Menu
def main():
    while True:
        print("\n--- Student Mark Management System ---")
        print("1. Input number of students and their information")
        print("2. Input number of courses and their information")
        print("3. Select a course and input marks for students")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a given course")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            input_number_of_students()
        elif choice == "2":
            input_number_of_courses()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_student_marks()
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
