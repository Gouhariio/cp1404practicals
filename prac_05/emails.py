def main():
    email_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        message = input("Is your name {}? (Y/n) ".format(name))
        if message.upper() != "Y":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")

    for email, name in email_name.items():
        print("{} ({})".format(name, email))


def get_name(email):
    prefix = email.split('@')[0]
    split = prefix.split('.')
    name = " ".join(split).title()
    return name

main()
