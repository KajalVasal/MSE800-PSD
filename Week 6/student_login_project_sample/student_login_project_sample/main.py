from users import (
    # import different functions from users.py
    student_login,
    submit_assignment,
    view_grades
)


def main():

    student_login("Mohammad")
    # call the student_login function with a sample username
    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    view_grades("Alex")


if __name__ == "__main__":
    main()
