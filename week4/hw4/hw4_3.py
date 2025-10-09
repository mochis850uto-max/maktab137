def most_frequent(list):
    most = list[0]
    max_count = 0
    for item in list:
        count = 0
        for i in list:
            if i == item:
                count += 1
                if count >= max_count:
                    max_count = count
                    most = item
    return most

result = most_frequent(["farm", "farm", "fish", "fruit", "farm"])
print(result)

result1 = most_frequent([2, 5, 8, 9, 2, 5, 2])
print(result1)