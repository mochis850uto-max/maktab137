def nested_sum(input):
    Sum_numbers = 0
    for item in input:
        if type(item) == list:
            Sum_numbers += nested_sum(item)
        else:
            Sum_numbers += item
    
    return Sum_numbers

result = nested_sum([1, [2, 3], [4, [5]]])
print(result)