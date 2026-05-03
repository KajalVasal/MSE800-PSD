import sqlite3
conn = sqlite3.connect('student_info.db')
cursor = conn.cursor()

# 1. Lecturers - must be first
cursor.execute('''
CREATE TABLE IF NOT EXISTS Lecturers (
    Lecturer_id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Department TEXT
);''')

# 2. Students  
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    Student_id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL
);''')

# 3. Course - needs Lecturers
cursor.execute('''
CREATE TABLE IF NOT EXISTS Course (
    Course_id INTEGER PRIMARY KEY,
    Course_name TEXT NOT NULL,
    Course_duration TEXT,
    Lecturer_id INTEGER,
    FOREIGN KEY (Lecturer_id) REFERENCES Lecturers(Lecturer_id)
);''')

# 4. Enrollment - needs Students + Course
cursor.execute('''
CREATE TABLE IF NOT EXISTS Enrollment (
    Enroll_id INTEGER PRIMARY KEY,
    Student_id INTEGER NOT NULL,
    Course_id INTEGER NOT NULL,
    Grade TEXT CHECK(Grade IN ('A+','A','B+','B','C+','C','D','E','F')),
    FOREIGN KEY (Student_id) REFERENCES Students(Student_id),
    FOREIGN KEY (Course_id) REFERENCES Course(Course_id),
    UNIQUE(Student_id, Course_id)
);''')  

conn.commit()
conn.close()
print("Database student_info.db created successfully")