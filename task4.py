# Task4_password_checker.py
# Made for SaiKet Systems Internship

def password_strength_checker():
    print("=== SaiKet Task 4: Password Strength Checker ===\n")
    
    password = input("Enter your password: ")
    
    # CRITERIA CHECK CHEYADAM
    has_length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    score = sum([has_length, has_upper, has_lower, has_digit, has_special])
    
    print("\n--- Password Analysis ---")
    print(f"Length >= 8        : {'✅' if has_length else '❌'}")
    print(f"Uppercase Letter   : {'✅' if has_upper else '❌'}")
    print(f"Lowercase Letter   : {'✅' if has_lower else '❌'}")
    print(f"Number             : {'✅' if has_digit else '❌'}")
    print(f"Special Character  : {'✅' if has_special else '❌'}")
    
    print(f"\nScore: {score}/5")
    
    # STRENGTH RATING
    if score == 5:
        print("Strength: 💪 VERY STRONG")
    elif score == 4:
        print("Strength: 👍 STRONG")
    elif score == 3:
        print("Strength: ⚠️ MEDIUM")
    elif score == 2:
        print("Strength: 👎 WEAK")
    else:
        print("Strength: ❌ VERY WEAK")
    
    print("\nMade for SaiKet Systems Internship")

if __name__ == "__main__":
    password_strength_checker()