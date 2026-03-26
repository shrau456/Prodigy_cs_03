# Prodigy_cs_01
# Password Complexity Checker
Password Complexity Checker is a Python-based command-line application that evaluates the strength of a password based on modern security standards. It provides a detailed analysis, including strength score, validation checks, and warnings for weak patterns.

# Features
- Analyzes password strength based on multiple criteria
- Length-based scoring system
- Detects uppercase and lowercase letters
- Checks for numeric characters
- Validates special characters
- Detects weak patterns:
  - Repeated characters (e.g., aaa)
  - Common sequences (123, abc, qwerty)
  - Single character-type passwords
- Provides strength rating:
  - Strong 
  - Medium 
  - Weak 
- Secure password input using getpass (hidden typing)
- Continuous CLI loop for multiple checks
# Tech Stack
- Language: Python
- Libraries Used:
  - re → Regular Expressions for pattern matching
  - getpass → Secure password input
  - sys → System exit handling
# Example Output
```
Password Complexity Checker
------------------------------

Enter password: ********

Result:
Strength: Medium (4/7)

Checks:
- ✓ Acceptable length (8+ characters)
- ✓ Contains lowercase letters
- ✗ Missing uppercase letters
- ✓ Contains numbers
- ✗ Missing special characters

Warnings:
- Repeated characters detected (e.g., aaa)
- Common sequence detected (e.g., 123, abc)
```
# Author 
- Created by : Suryawanshi Shravani Dnyanoba
- Task 3 : Password Complexity Checker - Completed 
