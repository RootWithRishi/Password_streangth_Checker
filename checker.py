import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    # Digit check
    if re.search(r"\d", password):
        strength += 1
    else:
        remarks.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character.")

    # Result
    if strength == 5:
        return "Strong Password"
    elif strength >= 3:
        return "Medium Password"
    else:
        return "Weak Password"

# User input
password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result)
