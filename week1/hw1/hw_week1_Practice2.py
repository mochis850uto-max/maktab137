number = input("please enter your number")
n: int = int(number)

user_number: int = 0
i = 1
while i < n:
    if n % i == 0:
        user_number += i
    i += 1

if user_number == n:
    print("yes")
else:
    print("no")
