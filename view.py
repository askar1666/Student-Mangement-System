def view_students(students):
    if not students:
        print("No students in the system.")
    else:
        print("\nList of students:")
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Scores: {student['scores']}")
