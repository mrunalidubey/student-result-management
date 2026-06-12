import sqlite3

def create_connection():
    conn = sqlite3.connect("student.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            branch TEXT
        );

        CREATE TABLE IF NOT EXISTS Subjects (
            subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL,
            max_marks INTEGER
        );

        CREATE TABLE IF NOT EXISTS Results (
            result_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject_id INTEGER,
            marks_obtained INTEGER,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
        );

        CREATE TABLE IF NOT EXISTS Attendance (
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject_id INTEGER,
            percentage REAL,
            FOREIGN KEY (student_id) REFERENCES Students(student_id),
            FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
        );
    ''')

    conn.commit()
    conn.close()
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()