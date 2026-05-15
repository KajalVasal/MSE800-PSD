from admin import check_user
from decorator import admin_required

@admin_required
def manage_zoo(user):
    """Admin-only function"""
    print(f"Welcome {user['role']}! You can manage animals and reports.")

def main():
    print("=== Zoo Admin Login ===")
    username = input("Username: ")
    password = input("Password: ")

    user = check_user(username, password)
    
    if user:
        print(f"Login successful. Hello {username}")
        manage_zoo(user)
    else:
        print("Login failed")

if __name__ == "__main__":
    main()