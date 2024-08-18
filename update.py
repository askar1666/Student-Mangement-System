def update_student_grade(students):
    name = input("Enter student name whose grade you want to update: ")
    for student in students:
        if student['name'] == name:
            subject = input("Enter the subject to update the grade for (Math, Science, English, History, Art): ")
            if subject in ["Math", "Science", "English", "History", "Art"]:
                index = ["Math", "Science", "English", "History", "Art"].index(subject)
                new_grade = float(input(f"Enter new grade for {subject}: "))
                student['scores'][index] = new_grade
                print(f"Grade for {subject} updated for {name}.")
                return
            else:
                print(f"Subject {subject} not found.")
                return
    print(f"Student {name} not found.")
