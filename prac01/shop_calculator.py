"""
CP1404/CP5632 - Practical
Program to determine total price
"""

items = int(input('Number of items: '))
total = 0.0
for prices in range(items):
    total += float(input('Price of item: '))
if total > 100:
    total = total - (total * 0.1)
print('Total price of three items ', "${:,.2f}".format(total))
