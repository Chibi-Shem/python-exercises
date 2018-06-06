

def get_ints(lst):
    """Removes non-integer elements from lst"""

    new_list = []
    for x in lst:
        if isinstance(x, int):
            new_list.append(x)
    return new_list


print(get_ints([1, 'a', 2, 3, '4']))
