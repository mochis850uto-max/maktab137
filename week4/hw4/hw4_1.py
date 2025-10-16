from datetime import datetime
time = datetime.now().hour

def restrict_hours(start, end):
    def decorator(func):
        def wrapper():
            if start <= time <= end:
                return func()
            
            else:
                print(f"The function is not running at this time.")
        return wrapper
    return decorator

@restrict_hours(start=9, end=16)
def do_work():
    print(f"working!")

do_work()    