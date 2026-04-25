# Updated ER Diagram With Lecturer Entity
Added lecturer entity

# Entities
1. **Student**: Student_id(PK),Name,Email
2. **Enrollment**: Enroll_id(PK),Student_id(FK),Course_id(FK),Grade
3. **Course**: Course_id(PK),Course_name,Course_duration,Lecturer_id(FK)
4. **Lecturer**: Lecturer_id(PK),Email,DEpartment,Name

# Relationships
1. Student 1:N
2. Course 1:N
3. Lecturer 1:N Course
