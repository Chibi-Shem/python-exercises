

def array_to_dict(keys, values):
    """Merges both lists and converts them into dictionary."""

    dct={}
    for x in range(len(keys)):
    	dct.update({keys[x]: values[x]})
    return dct


print(array_to_dict(['a', 'b', 'c'],[1, 2, 3]))
