# Updated ER Diagram With Lecturer Entity
Added lecturer entity

# Entities
1. **Student**: Student_id(PK),Name,Email Unique
2. **Enrollment**: Enroll_id(PK),Student_id(FK),Course_id(FK),Grade
3. **Course**: Course_id(PK),Course_name,Course_duration,Lecturer_id(FK)
4. **Lecturer**: Lecturer_id(PK),Email,Department,Name

# Relationships
1. Student 1:N
2. Course 1:N
3. Lecturer 1:N Course

# How to Run 
1. Create the database and tables using the provided SQL code.
2. Insert data into the tables 
3. Run the SQL queries
