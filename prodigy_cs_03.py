import re
import sys
from getpass import getpass

def analyze_password(password):
    if not password:
        raise ValueError("Password cannot be empty")

    score = 0
    details = []
    warnings = []

    # Length check
    length = len(password)
    if length >= 12:
        score += 3
        details.append("✓ Strong length (12+ characters)")
    elif length >= 8:
        score += 2
        details.append("✓ Acceptable length (8+ characters)")
    else:
        details.append("✗ Too short (minimum 8 characters)")

    # Character checks
    checks = {
        "uppercase": (r"[A-Z]", "uppercase letters"),
        "lowercase": (r"[a-z]", "lowercase letters"),
        "numbers": (r"[0-9]", "numbers"),
        "special": (r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", "special characters")
    }

    for key, (pattern, label) in checks.items():
        if re.search(pattern, password):
            score += 1
            details.append(f"✓ Contains {label}")
        else:
            details.append(f"✗ Missing {label}")

    # Pattern warnings
    if re.search(r"(.)\1{2,}", password):
        warnings.append("Repeated characters detected (e.g., aaa)")

    if re.search(r"(123|abc|qwerty)", password.lower()):
        warnings.append("Common sequence detected (e.g., 123, abc)")

    if password.islower() or password.isupper() or password.isdigit():
        warnings.append("Only one type of character used")

    if length > 50:
        warnings.append("Password unusually long")

    # Strength classification
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    else:
        strength = "Weak"

    return score, strength, details, warnings


def run_checker():
    print("Password Strength Analyzer")
    print("-" * 30)
    print("Type 'exit' to quit.\n")

    while True:
        try:
            pwd = getpass("Enter password: ")

            if pwd.lower() == "exit":
                print("\nExiting...")
                break

            score, strength, details, warnings = analyze_password(pwd)

            print("\nResult:")
            print(f"Strength: {strength} ({score}/7)\n")

            print("Checks:")
            for d in details:
                print(" ", d)

            if warnings:
                print("\nWarnings:")
                for w in warnings:
                    print(" ", w)

            print("\n" + "=" * 50)

        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            sys.exit(0)

        except Exception as e:
            print(f"Error: {e}\nTry again.\n")


if __name__ == "__main__":
    run_checker()