out_file = open("name.txt", 'w')
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()
reader = open("name.txt", 'r')
print("Your name is ", reader.read())
reader.close()
numbers = open("number.txt", 'w')
print("17 \n 42 \n 400", file = numbers)
numbers.close()
number_reader = open("number.txt", 'r')
number_reader.close()
