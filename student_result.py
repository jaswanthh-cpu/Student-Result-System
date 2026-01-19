students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = []

    for i in range(5):
        m = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    total = sum(marks)
    percentage = total / 5

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    student = {
        "Name": name,
        "Roll": roll,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No student records found.\n")
        return

    for s in students:
        print("------------------------")
        for key, value in s.items():
            print(f"{key}: {value}")
        print("------------------------\n")

while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice\n")
