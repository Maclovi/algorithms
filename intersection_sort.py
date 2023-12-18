def intersection_sort(lst):
    def find_min_elem(lst2):
        element = lst2[0]
        position = 0
        for i in range(len(lst2)):
            if lst2[i] < element:
                element = lst2[i]
                position = i
        return position, element

    lst = lst.copy()
    sort_result = []
    while lst:
        index, elem = find_min_elem(lst)
        del lst[index]
        sort_result.append(elem)

    return sort_result
