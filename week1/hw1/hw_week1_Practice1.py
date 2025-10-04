name: str = input("please enter your name")
user_name: list = list(name)
print(user_name)

index: int = 0
while index < len(user_name):
    if user_name[index] == " ":
        del user_name[index]

    elif user_name[index] == "a" or user_name[index] == "A":
        user_name[index] = "."

    elif user_name[index] == "e" or user_name[index] == "E":
        user_name[index] = "."

    elif user_name[index] == "i" or user_name[index] == "I":
        user_name[index] = "."

    elif user_name[index] == "u" or user_name[index] == "U":
        user_name[index] = "."

    elif user_name[index] == "o" or user_name[index] == "O":
        user_name[index] = "."

    index += 1

user_name.reverse()
print(user_name)
result = ''.join(map(str, user_name))

print(result)





