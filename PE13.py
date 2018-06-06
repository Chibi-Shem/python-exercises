

def check_difference(lst, lst2):
    """Returns the values from array that
    are not present in the other arrays.
    """

    new_list = []
    for x in lst:
        if lst2.count(x)==0:
        	new_list.append(x)
    return new_list


print(check_difference([1, 2, 3, '4'], [2, 3, 10]))
