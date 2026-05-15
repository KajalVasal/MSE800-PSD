from datetime import datetime

def log_activity(func):

    def wrapper(*args, **kwargs):
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")
        # Call the original function and store the result
        result = func(*args, **kwargs)
        
        print("Activity completed.")
        print("===================================\n")

        return result
        # Return the result of the original function call
    return wrapper
