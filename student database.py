import mysql.connector

student_details = {}
while True:import mysql.connector

student_details = {}
while True:
    print(" Student Management System ")
    print(" 1. All students")
    print(" 2. View All students")
    print(" 3. Search Student")
    print(" 4. Delete Student")
    print(" 5. Exit")

    choice = input("Enter choice ( 1 - 5 ) : ")

    if choice == "1":
        roll_no = input("Enter roll number:")
        if roll_no in choice:
            print("student_details only exist")
        else:
            name = input("Enter Name: ")
            grade = input("Enter Course : ")
            student_details[roll_no] = {"name": name, "grade": grade}
            print(f"Student '{name}' added successfully.")

    elif choice == "2":
        if not student_details:
            print("No student records found.")
        else:
            print("\nRoll No       | Name           | Course           ")
            print("-" * 25)
            for roll_no, info in student_details.items():
                print(f"{roll_no:<7} | {info['name']:<10} | {info['grade']}")

    elif choice == "3":
        roll_no = input("Enter Roll Number to search: ")
        if roll_no in student_details:
            info = student_details[roll_no]
            print(f"Found: Name: {info['name']}, Grade: {info['grade']}")
        else:
            print("Student not found.")

    elif choice == "4":
        roll_no = input("Enter Roll Number to delete: ")
        if roll_no in student_details:
            del student_details[roll_no]
            print("Student record deleted.")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1 to 5.")  
    print(" Student Management System ")
    print(" 1. All students")
    print(" 2. View All students")
    print(" 3. Search Student")
    print(" 4. Delete Student")
    print(" 5. Exit")

    choice = input("Enter choice ( 1 - 5 ) : ")

    if choice == "1":
        roll_no = input("Enter roll number:")
        if roll_no in choice:
            print("student_details only exist")
        else:
            name = input("Enter Name: ")
            grade = input("Enter Course : ")
            student_details[roll_no] = {"name": name, "grade": grade}
            print(f"Student '{name}' added successfully.")

    elif choice == "2":
        if not student_details:
            print("No student records found.")
        else:
            print("\nRoll No       | Name           | Course           ")
            print("-" * 25)
            for roll_no, info in student_details.items():
                print(f"{roll_no:<7} | {info['name']:<10} | {info['grade']}")

    elif choice == "3":
        roll_no = input("Enter Roll Number to search: ")
        if roll_no in student_details:
            info = student_details[roll_no]
            print(f"Found: Name: {info['name']}, Grade: {info['grade']}")
        else:
            print("Student not found.")

    elif choice == "4":
        roll_no = input("Enter Roll Number to delete: ")
        if roll_no in student_details:
            del student_details[roll_no]
            print("Student record deleted.")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1 to 5.")  
