import random


def quick_sort(lst):
    if len(lst) < 2:
        return lst
    pivot = lst.pop(random.randrange(len(lst)))
    less = list(filter(lambda x: x <= pivot, lst))
    greater = list(filter(lambda x: x > pivot, lst))
    return quick_sort(less) + [pivot] + quick_sort(greater)
