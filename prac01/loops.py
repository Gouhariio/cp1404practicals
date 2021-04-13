"""
CP1404/CP5632 - Practical
Program for loops
"""

print('a.')
for i in range(10, 101, 10):
    print(i, end=' ')
print('\n', 'b.')
num = 20
while num > 0:
    print(num)
    num = num - 1
print(num, end ='\r')
print('c.')
num_stars = int(input('Number of stars: '))
for output in range (num_stars):
    print("* ", end="")
print('\n', 'd.')
rows = int(input('Enter the number of rows, please '))
stars = 1
for lines in range(0, rows):
    for result in range(0, stars):
      print("* ", end="")
    stars = stars + 1
    print()