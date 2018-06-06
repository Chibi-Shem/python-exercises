

def find_object(lst, obj):
    """Returns the first value in lst that
    matches the key-value pair in obj.
    """

    try:
        for x in lst:
            if x.items().count(obj.items()[0]) >= 1:
                return x
        return str(obj) + ' is not in list.'
    except:
        return str(obj) + ' is not in list.'


print(find_object([
            {1: 'one', 'index': 0},
            {2: 'two', 'index': 1},
            {3: 'three', 'index': 2}
            ],
            {'index': 2}))
