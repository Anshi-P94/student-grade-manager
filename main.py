import json
class StudentManager:
    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        try:
            with open("students.json","r") as file:
                self.students = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []

    def save_data(self):
        with open("students.json", "w") as file:
            json.dump(self.students, file, indent=4)

    def find_student_by_roll(self, roll):
        for student in self.students:
            if student["roll"] == roll:
                return student
        return None

    def print_student(self, student, count=None):
        if count is not None:
            print(f"\nStudent {count}")
        print("-" * 20)
        print(f"Name       : {student['name']}")
        print(f"Roll No.   : {student['roll']}")
        print(f"Department : {student['department']}")
        print(f"Grade      : {student['grade']}")

    def add_student(self):
        while True:
            name = input("Enter student name: ").strip()
            if name:
                break
            print("Name cannot be empty.")
        while True:
            roll = input("Enter student roll number: ").strip()
            if self.find_student_by_roll(roll):
                print("Roll Number already exists. Try again.")
            else:
                break
        while True:
            dep = input("Department: ").strip()
            if dep:
                break
            print("Department cannot be empty.")
        while True:
            grade = input("Enter student grade: ")
            try:
                grade = float(grade)
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
        self.students.append({
            "name": name,
            "roll": roll,
            "department": dep,
            "grade": grade
        })
        self.save_data()
        print(f"Student {name} added successfully!")

    def view_students(self):
        if not self.students:
            print("\nNo student available.\n")
        else:
            for count, student in enumerate(self.students, start=1):
                self.print_student(student, count)

    def search_student(self):
        roll = input("Roll No. To Be Searched: ").strip()
        student = self.find_student_by_roll(roll)
        if student:
            self.print_student(student)
        else:
            print("Student Not Found")

    def delete_student(self):
        roll = input("Roll No. To Be Deleted: ").strip()
        student = self.find_student_by_roll(roll)
        if student:
            self.students.remove(student)
            self.save_data()
            print(f"{student['name']} deleted successfully.")
        else:
            print("Student Not Found")

    def update_student(self):
        roll = input("Enter Roll Number to Update: ").strip()
        student = self.find_student_by_roll(roll)
        if student:
            print("\nPress Enter to keep existing value.\n")
            name = input(f"Name ({student['name']}): ").strip()
            department = input(f"Department ({student['department']}): ").strip()
            while True:
                grade = input(f"Grade ({student['grade']}): ")
                if grade == "":
                    break
                try:
                    grade = float(grade)
                    if 0 <= grade <= 100:
                        break
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")
            if name:
                student["name"] = name
            if department:
                student["department"] = department
            if grade != "":
                student["grade"] = grade
            self.save_data()
            print("Student Updated Successfully!")
        else:
            print("Student Not Found")

    def statistics(self):
        if not self.students:
            print("No students available.")
            return
        total_students = len(self.students)
        average_grade = sum(student["grade"] for student in self.students) / len(self.students)
        highest = max(self.students, key=lambda student: student["grade"])
        lowest = min(self.students, key=lambda student: student["grade"])
        a_grade_students = sum(1 for student in self.students if student["grade"] >= 90)
        print("=" * 30)
        print("Student Statistics")
        print("=" * 30)
        print("Total Students :", total_students)
        print("Average Grade  :", round(average_grade, 2))
        print("Highest Grade  :", highest["grade"])
        print("Lowest Grade   :", lowest["grade"])
        print("\nTop Student")
        print("-" * 20)
        print("Name             :", highest["name"])
        print("Roll No.         :", highest["roll"])
        print("Department       :", highest["department"])
        print("Grade            :", highest["grade"])
        print("\nGrade Distribution")
        print("-" * 20)
        a = 0
        b = 0
        c = 0
        d = 0
        f = 0
        for student in self.students:
            grade = student["grade"]
            if grade >= 90:
                a += 1
            elif grade >= 80:
                b += 1
            elif grade >= 70:
                c += 1
            elif grade >= 60:
                d += 1
            else:
                f += 1
        print("A (90-100):", a)
        print("B (80-89) :", b)
        print("C (70-79) :", c)
        print("D (60-69) :", d)
        print("F (<60)   :", f)
        print(f"A Grade Students : {a_grade_students}")   

manager = StudentManager()
def main():
    while True:
        print("=" * 30)
        print("Student Grade Manager")
        print("=" * 30)

        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Statistics")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            manager.add_student()

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            manager.search_student()

        elif choice == "4":
            manager.delete_student()

        elif choice == "5":
            manager.update_student()

        elif choice == "6":
            manager.statistics()

        elif choice == "7":
            print("Thank you for using Student Grade Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()