text_dict = dict()
text = input("Enter the text: ")
words = text.split(" ")
for word in words:
        if word in text_dict:
            text_dict[word] = text_dict[word] + 1
        else:
            text_dict[word] = 1

for key in list(text_dict.keys()):
    print(key, ":", text_dict[key])
