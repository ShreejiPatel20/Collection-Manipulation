students=[]
while True:
    print("\nWelcome to the Student Data Organizer!")
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice==1:
        print("\nEnter student details:")
        student = {}
        student["id"]=input("Student ID: ")
        student["name"]=input("Name: ")
        student["age"]=input("Age: ")
        student["grade"]=input("Grade: ")
        student["dob"]=input("Date of Birth (YYYY-MM-DD): ")
        subjects=input("Subjects (comma-separated): ")
        student["subjects"]=[s.strip() for s in subjects.split(",")]

        students.append(student)
        print("\nStudent added successfully!")

    elif choice==2:
        print("\n--- Display All Students ---")
        if len(students)==0:
            print("No students found.")
        else:
            for s in students:
                print(f"Student ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {', '.join(s['subjects'])}")

    elif choice==3:
        sid=input("Enter Student ID to update: ")
        found = False
        for s in students:
            
            if s["id"]==sid:
                found = True
                student["name"] = input("New Name: ")
                student["age"] = input("New Age: ")
                student["grade"] = input("New Grade: ")
                student["dob"] = input("New DOB (YYYY-MM-DD): ")
                subjects = input("New Subjects (comma-separated): ")
                student["subjects"] = [sub.strip() for sub in subjects.split(",")]
                print("Student updated successfully!")
                break
        if not found:
            print("Student not found.")

    elif choice==4:
        sid=input("Enter Student ID to delete: ")
        found=False
        for s in students:
            if s["id"]==sid:
                students.remove(s)
                found=True
                print("Student deleted successfully!")
                break
        if not found:
            print("Student not found.")

    elif choice==5:
        subjects_set = set()
        for s in students:
            subjects_set.update(s["subjects"])

        print("\nSubjects Offered:")
        if len(subjects_set)==0:
            print("No subjects available.")
        else:
            for sub in sorted(subjects_set):
                print(sub)

    elif choice==6:
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please try again.")
 