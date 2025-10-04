def number(x):

    if x >= 1:
        return f"{x}"
    else:
        raise ValueError("This number is not correct")
        

   
user_number = int(input("Enter your number"))
result = number(user_number)
print(result)