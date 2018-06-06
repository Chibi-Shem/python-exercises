

def list_to_int(lst):
    """Converts a list of integers lst into a single integer."""
    single_int = ''
    for x in range(len(lst)):
        single_int += str(lst[x])
    return int(single_int)


lst = [1, 2, 3, 5, 6]
print(list_to_int(lst))
