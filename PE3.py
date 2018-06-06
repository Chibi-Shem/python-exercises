

def list_odd(lst):
    """Returns a list of odd numbers from list lst."""
    odd_list = []
    for x in range(len(lst)):
        if(lst[x] % 2 != 0):
            odd_list.append(lst[x])
    return odd_list


lst = [1, 2, 3, 5, 6]
print(list_odd(lst))
