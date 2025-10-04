import itertools
import copy

# sentence = input("Enter a sentence or a few words: ")

# words = sentence.split()


def extract_words(words, x):
    # for i in itertools.combinations(words, x):
    #     yield list(i)
    yield x
    yield words
result = extract_words(["apple", "fish"], 2)
print(result)
words_list = []
# for x in [2, 3, 4]:
#     words_list.extend(list(extract_words(words, x)))


# shallow_copy = copy.copy(words_list)
# deep_copy = copy.deepcopy(words_list)

# # print("Main list before shallow copy: ", words_list)
# # shallow_copy[0][0] = "maktab137"
# # print("Main list after shallow copy: ", words_list)
# # print("Shallow Copy:", shallow_copy)

# print("Main list before deep copy: ", words_list)
# deep_copy[0][0] = "maktab137"
# print("Main list after deep copy: ", words_list)
# print("deep Copy:",deep_copy)