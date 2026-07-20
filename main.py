students =[]
def  main():
    while True:
        print("="*30)
        print("Student Grade Manager")
        print("="*30)
        print()

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")  
        print("4. Delete Student")
        print("5. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            name = input("Enter student name: ")
            roll = input("Enter student roll number: ")
            dep = input("Enter student department: ")
            grade = input("Enter student grade: ")
            students.append({"name": name,"roll": roll,"department": dep,"grade": grade})
            print(f"Student {name} added successfully!")

        elif choice == "2":
            if not students:
                print("\nNo student available.\n")
            else:
                count = 1
                for student in students:
                    print(f"\nStudent {count}")
                    print("-" * 20)
                    print("Name       :",student["name"])
                    print("Roll No.   :",student["roll"])
                    print("Department :",student["department1"])
                    print("Grade      :",student["grade"])
                    count += 1

        elif choice == "3":
            print("Feature coming soon...")

        elif choice == "4":
            print("Feature coming soon...")

        elif choice == "5":
            print("Thank you for using Student Grade Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

