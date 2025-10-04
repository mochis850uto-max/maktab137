def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for x in range(0, n-i-1):
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
    return arr
result = bubble_sort([5, 1, 4])
print(result)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    print(pivot)
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1]if x > pivot]
    print(f"pivot = {pivot}, left = {left}, right = {right}")
    return quick_sort(left) + [pivot] + quick_sort(right)
result = quick_sort([8, 3, 9, 7])
print(result)
