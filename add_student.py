def add_student(students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    subjects = ["Math", "Science", "English", "History", "Art"]
    scores = []

    for subject in subjects:
        score = float(input(f"Enter {subject} score: "))
        scores.append(score)

    student = {"name": name, "age": age, "scores": scores}
    students.append(student)
    print(f"Student {name} added successfully.")
