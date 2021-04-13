minimum = 10
password = input("Enter password of at least {} characters: ".format(minimum))
while len(password) < minimum:
    print('password is too short')
    password = input("Enter password of at least {} characters: ".format(minimum))

print('*' * len(password))