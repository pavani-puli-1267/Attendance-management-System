students = []
attendance = {}

while True:

    print("\n===== ATTENDANCE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Save Attendance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully")

    elif choice == "2":
        print("\nStudents List:")

        if len(students) == 0:
            print("No students found")

        else:
            for student in students:
                print(student)

    elif choice == "3":
        name = input("Enter student name: ")

        if name in students:
            status = input("Enter Present or Absent: ")
            attendance[name] = status
            print("Attendance marked successfully")

        else:
            print("Student not found")

    elif choice == "4":

        print("\nAttendance Records:")

        if len(attendance) == 0:
            print("No attendance records")

        else:
            for student, status in attendance.items():
                print(student, "-", status)

    elif choice == "5":

        file = open("attendance.txt", "w")

        for student, status in attendance.items():
            file.write(student + " - " + status + "\n")

        file.close()

        print("Attendance saved successfully")

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")