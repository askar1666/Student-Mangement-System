def calculate_individual_average_grade(students):
    name = input("Enter student name to calculate individual average grade: ")
    for student in students:
        if student['name'] == name:
            average_grade = sum(student['scores']) / len(student['scores'])
            print(f"Individual average grade for {name}: {average_grade:.2f}")
            return
    print(f"Student {name} not found.")
