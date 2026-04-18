#  Program to collect and display student information 
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        
# function
def collect_student_info():
    students = []
    for i in range(3):
        print(f"\nEnter details for student {i+1}:")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        student_id = input("Enter student ID: ")
        student = Student(name, age, student_id)
        students.append(student)
    return students

# Sort students by age 
def display_students(students):
    sorted_students = sorted(students, key=lambda s: s.age)
    
    print("\nStudent information sorted by age:")
    for student in sorted_students:
        print(f" Name:{student.name}, Age:{student.age}")
       
       
# Main function 
def main():
    student_list = collect_student_info()
    display_students(student_list)    
if __name__ == "__main__":
        main()
        