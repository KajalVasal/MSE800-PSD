# Store user credentials and roles
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "guest": {"password": "guest123", "role": "guest"}
}

def check_user(username, password):
    """Check if username/password is valid and return user data"""
    user = USERS.get(username)
    if user and user["password"] == password:
        return user
    return None