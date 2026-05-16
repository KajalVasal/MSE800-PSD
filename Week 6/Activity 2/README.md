# Zoo Admin Login System
A simple Python project that demonstrates role-based access control using a decorator.

## Project Structure
zoo-admin-login/
**main.py**      # Main program with login and menu
**admin.py**     # User data and authentication logic  
**decorator.py**  # Custom decorator for admin access control
**README.md**     # Project documentation

## Functionality
1. **Login**: Users enter username and password to log in.
2. **Role Check**: The system checks if the user has the `admin` role.
3. **Access Control**: Only admins can access protected functions. Others get an access denied message.

## How the Decorator Works
The `admin_required` decorator in `decorator.py` wraps any function that should be restricted to admins.

**Flow:**
1. User logs in via `check_user` in `admin.py`.
2. When an admin-only function is called, the decorator runs first.
3. It checks `user["role"]`. 
   - If `admin` → runs the function.
   - If not → prints "Access Denied" and stops execution.

This keeps access logic separate from business logic.

## How to Run
1. Open VSCode.
2. Run:
   python main.py

