def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        middle = (low + high) // 2
        if lst[middle] == item:
            return middle
        if item > lst[middle]:
            low = middle + 1
        else:
            high = middle - 1
