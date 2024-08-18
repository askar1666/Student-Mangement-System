from add_student import add_student
from view_students import view_students
from update_student_grade import update_student_grade
from delete_student import delete_student
from calculate_individual_average_grade import calculate_individual_average_grade

def main():
    students = []  # Initialize an empty list to store student records

    while True:
        print("\nStudent Management System Menu:")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Grade")
        print("4. Delete Student")
        print("5. Calculate Individual Average Grade")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            add_student(students)
        elif choice == 2:
            view_students(students)
        elif choice == 3:
            update_student_grade(students)
        elif choice == 4:
            delete_student(students)
        elif choice == 5:
            calculate_individual_average_grade(students)
        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
