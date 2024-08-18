def delete_student(students):
    name = input("Enter student name to delete: ")
    for i, student in enumerate(students):
        if student['name'] == name:
            del students[i]
            print(f"Student {name} deleted.")
            return
    print(f"Student {name} not found.")
