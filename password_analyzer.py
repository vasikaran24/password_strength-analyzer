import re

def analyze_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase password length (at least 8–12 characters).")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    # Special characters
    if re.search(r"[!@#$%^&*()_+|}{\":?><,./;'[\]\\]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$...).")

    # Common weak patterns
    common_patterns = ["1234", "password", "admin", "qwerty"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 1
        feedback.append("Avoid common patterns like '1234' or 'password'.")

    # Strength classification
    if score <= 1:
        strength = "Very Weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback


def suggest_password():
    return "Example strong password: pA4$aoem23X!"


# Main program
if __name__ == "__main__":
    password = input("Enter your password: ")

    strength, feedback = analyze_password(password)

    print("\n🔍 Password Strength:", strength)

    if feedback:
        print("\n⚠️ Suggestions to improve:")
        for f in feedback:
            print("-", f)

    if strength in ["Very Weak", "Weak"]:
        print("\n💡 Suggested Password:")
        print(suggest_password())
