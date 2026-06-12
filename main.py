from database import create_tables
from students import add_student, view_all_students, delete_student
from results import add_subject, add_result, view_results, top_students, average_marks_per_branch

def main():
    create_tables()
    while True:
        print("""
--- Student Result Management System ---
1. Add Student
2. View All Students
3. Delete Student
4. Add Subject
5. Add Result
6. View Results (Pass/Fail)
7. Top 3 Students
8. Average Marks Per Branch
9. Exit
        """)
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            branch = input("Enter branch: ")
            add_student(name, age, branch)

        elif choice == "2":
            view_all_students()

        elif choice == "3":
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)

        elif choice == "4":
            subject_name = input("Enter subject name: ")
            max_marks = int(input("Enter max marks: "))
            add_subject(subject_name, max_marks)

        elif choice == "5":
            student_id = int(input("Enter student ID: "))
            subject_id = int(input("Enter subject ID: "))
            marks = int(input("Enter marks obtained: "))
            add_result(student_id, subject_id, marks)

        elif choice == "6":
            view_results()

        elif choice == "7":
            top_students()

        elif choice == "8":
            average_marks_per_branch()

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()