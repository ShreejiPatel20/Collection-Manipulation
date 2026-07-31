# Student Data Organizer

students = []
student_dict = {}
subjects_set = set()

print("=" * 50)
print("Welcome to the Student Data Organizer!")
print("This program manages student records.")
print("=" * 50)

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice==1:

        print("\nEnter student details:")
        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subject_input = input("Subjects (comma-separated): ")
        subject_list = [i.strip() for i in subject_input.split(",")]
        subjects_set.update(subject_list)
        student_tuple = (student_id, dob)

        student = {"id": student_id, "name": name,"age": age,"grade": grade,"subjects": subject_list,"details": student_tuple}
        
        students.append(student)
        student_dict[student_id] = { "name": name,"age": age,"grade": grade,"subjects": subject_list}
        
        print("\nStudent added successfully!")
    elif choice == 2:
        print("\n--- Display All Students ---")
        if len(students) == 0:
            print("No student records found.")
        else:
            for s in students:
                sid, dob = s["details"]
                print( f"Student ID: {sid} | "f"Name: {s['name']} | "f"Age: {s['age']} | "f"Grade: {s['grade']} | "f"Subjects: {', '.join(s['subjects'])}")
    elif choice==3:

        sid = int(input("Enter Student ID to update: "))
        found = False
        for s in students:
            if s["id"] == sid:
                found = True
                print("\n1. Update Age")
                print("2. Update Subjects")
                option = int(input("Enter choice: "))

                if option==1:
                    new_age = int(input("Enter new age: "))
                    s["age"] = new_age
                    student_dict[sid]["age"] = new_age
                    print("Age updated successfully.")

                elif option==2:
                    new_subjects = input("Enter new subjects (comma-separated): ")
                    subject_list = [i.strip() for i in new_subjects.split(",")]
                    s["subjects"] = subject_list
                    student_dict[sid]["subjects"] = subject_list
                    subjects_set.update(subject_list)
                    print("Subjects updated successfully.")
                else:
                    print("Invalid option.")
                break

        if not found:
            print("Student ID not found.")
    elif choice == 4:
        sid = int(input("Enter Student ID to delete: "))
        found = False
        for i in range(len(students)):
            if students[i]["id"] == sid:
                del students[i]
                if sid in student_dict:
                    del student_dict[sid]
                print("Student deleted successfully.")
                found = True
                break

        if not found:
            print("Student ID not found.")
    elif choice == 5:
        print("\nUnique Subjects Offered:")
        if len(subjects_set) == 0:
            print("No subjects available.")
        else:
            for subject in sorted(subjects_set):
                print(subject)
    elif choice == 6:

        print("\nThank you for using the Student Data Organizer!")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")