def simple_calculator(*args, **kwargs):
    if kwargs["operator"] == "+":
        result = args[0] + args[1]
        return result
    elif kwargs["operator"] == "-":
        result = args[0] - args[1]
        return result
    elif kwargs["operator"] == "*":
        result = args[0] * args[1]
        return result
    elif kwargs["operator"] == "/":
        result = args[0] / args[1]
        return result
    else:
        print("invalid operator")

print(simple_calculator(10, 5, operator = "*"))