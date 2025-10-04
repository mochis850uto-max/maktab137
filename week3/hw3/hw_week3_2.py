import copy 


words = input("Enter a few words: ")

words = words.lower()

words_list = words.split()

words_list = [i for i in words_list if i not in("!", "?", ".", ",")]

print(words_list)


def cache_decorator(func):
    cache = {}
    
    def wrapper(*args):
       result = func(*args)
       key = tuple(args[0])
       if key in cache:
           print(cache)
           return copy.deepcopy(cache[key])        
       else:
           result = func(*args)
           cache[key] = copy.deepcopy(result)
           return copy.deepcopy(result)
    return wrapper


        
@cache_decorator
def count_words_list(words_list):
    counts = {}

    for word in words_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

result = count_words_list(words_list)
print(result)

result = count_words_list(words_list)
print(result)
