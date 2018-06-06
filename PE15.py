

def print_in_pairs(lst, lst2):
    """Prints lst and lst2 elements in pairs."""

    for x in range(len(lst)):
    	print(str(lst[x])+' '+str(lst2[x]))


print_in_pairs(['a', 'b', 'c'], [1, 2, 3])
