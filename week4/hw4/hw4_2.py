def cast_to_string(func):
    def wrapper(*args, **kwargs):
        str_args = []
        for i in args:
            str_args.append(i)

        str_kwargs = {}
        for k, v in kwargs.items():
            str_kwargs[k] = str(v)
        return func(*str_args,**str_kwargs)
    return wrapper

def length_string(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f"length '{arg}': {len(str(arg))}")
        for k, v in kwargs.items():
            print(f"length '{k}': {len(str(k))}")
            print(f"length '{v}': {len(str(v))}")
            result = func(*args, **kwargs)
        return result
    return wrapper

@cast_to_string
@length_string
def information(*args, **kwargs):
    print(args, kwargs)

information(2, "farmer", a = 12, score = 50.2)