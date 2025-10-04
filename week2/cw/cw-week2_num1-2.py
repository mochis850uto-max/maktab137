try:
     #  imput number
     num = float(input("enter a number: "))
     num2 = float(input("enter a number: "))

     result = num / num2
     print(f" {result}")


except ZeroDivisionError:

 print("you can't divide by zero")


# 2.
try:
    user_input = input("enter a number: ")
    number = int(float(user_input))
    print(f" {number}")


    number = int(user_input)

    print(f" {number}")

except ValueError:
    print(" just number!")
    