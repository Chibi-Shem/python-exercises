

def contains(lst, obj):
    """Return True if the value is present in the list."""

    try:
        for x in lst:
            if obj == x:
                return True
        return False
    except:
        return False


print(contains([1, 2, 3, '4'], '4'))
