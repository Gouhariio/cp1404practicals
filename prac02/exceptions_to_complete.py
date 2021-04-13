"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        number = int(input("Enter the number: "))
        result = number
        print("Valid result is:", result)
    except  ValueError:
           print("Please enter a valid integer.")
