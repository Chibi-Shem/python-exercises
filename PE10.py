

def find_index(lst, obj):
    """Returns the index number of an object in lst."""

    try:
        return lst.index(obj)
    except:
        return str(obj) + ' is not in list.'


print(find_index([1, 2, 3, 4, 1, 2], 2))
