"""
CP1404/CP5632 - Practical
Program to determine score status
"""


score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif 50 <= score < 90:
    print("Passable")
elif 90 <= score <= 100:
    print("Excellent")
else:
    print("Bad")
