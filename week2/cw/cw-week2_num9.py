book: dict ={
    "name":"bright nights",
    "author":"Fyodor Dostoevsky",
    "release":1848
    }

def saved_to_json(data, file_name):
    whit.open(file_name, 'w')
        json.dump(data, file_name)
    print(f"date saved to"{json})


