"""
Name: Guoming Liao
Date: 10-9-24
Description: User role ID matchup admin
"""

role = input("What is your role?: ").title()
id = int(input("What is your ID?: "))

if role == "Admin" and id == 1:
    print("super admin given")

elif role == "Admin" or 2 <= id <= 100:
    print("admin given")