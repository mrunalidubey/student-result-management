from database import create_connection

def add_student(name, age, branch):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (name, age, branch) VALUES (?, ?, ?)", 
                   (name, age, branch))
    conn.commit()
    conn.close()
    print(f"Student '{name}' added successfully.")

def view_all_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    if students:
        print("\n--- All Students ---")
        for s in students:
            print(f"ID: {s[0]} | Name: {s[1]} | Age: {s[2]} | Branch: {s[3]}")
    else:
        print("No students found.")

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE student_id=?", (student_id,))
    conn.commit()
    conn.close()
    print(f"Student ID {student_id} deleted.")