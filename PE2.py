

def insert(lst, x):
    """Inserts variable x into list lst without using append."""
    return lst + [x]


lst = [1, 2, 3]
print(insert(lst, 4))
