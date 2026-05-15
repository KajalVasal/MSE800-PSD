def admin_required(func):
    """Decorator: only allows users with role 'admin' to run the function"""
    def wrapper(user):
        if not user:
            print("Error: Not logged in")
            return
        if user["role"] != "admin":
            print("Access Denied: Admins only!")
            return
        return func(user)
    return wrapper