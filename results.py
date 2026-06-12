from database import create_connection

def add_subject(subject_name, max_marks):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Subjects (subject_name, max_marks) VALUES (?, ?)",
                   (subject_name, max_marks))
    conn.commit()
    conn.close()
    print(f"Subject '{subject_name}' added successfully.")

def add_result(student_id, subject_id, marks_obtained):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Results (student_id, subject_id, marks_obtained) VALUES (?, ?, ?)",
                   (student_id, subject_id, marks_obtained))
    conn.commit()
    conn.close()
    print("Result added successfully.")

def view_results():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.name, sub.subject_name, r.marks_obtained, sub.max_marks,
        CASE WHEN r.marks_obtained >= sub.max_marks * 0.4 THEN "PASS" ELSE "FAIL" END as status
        FROM Results r
        JOIN Students s ON r.student_id = s.student_id
        JOIN Subjects sub ON r.subject_id = sub.subject_id
    ''')
    results = cursor.fetchall()
    conn.close()
    if results:
        print("\n--- Results ---")
        for r in results:
            print(f"Student: {r[0]} | Subject: {r[1]} | Marks: {r[2]}/{r[3]} | Status: {r[4]}")
    else:
        print("No results found.")

def top_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.name, sub.subject_name, r.marks_obtained
        FROM Results r
        JOIN Students s ON r.student_id = s.student_id
        JOIN Subjects sub ON r.subject_id = sub.subject_id
        ORDER BY r.marks_obtained DESC
        LIMIT 3
    ''')
    results = cursor.fetchall()
    conn.close()
    print("\n--- Top 3 Students ---")
    for r in results:
        print(f"Name: {r[0]} | Subject: {r[1]} | Marks: {r[2]}")

def average_marks_per_branch():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.branch, ROUND(AVG(r.marks_obtained), 2) as avg_marks
        FROM Results r
        JOIN Students s ON r.student_id = s.student_id
        GROUP BY s.branch
    ''')
    results = cursor.fetchall()
    conn.close()
    print("\n--- Average Marks Per Branch ---")
    for r in results:
        print(f"Branch: {r[0]} | Average Marks: {r[1]}")