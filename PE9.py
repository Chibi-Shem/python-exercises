

def get_unique(lst):
    """Removes duplicate objects in lst."""

    new_list=[]
    for x in range(len(lst)):
    	if lst.count(lst[x]) == 1:
	    	new_list.append(lst[x])
    return new_list


print(get_unique([1, 2, 3, 4, 1, 2]))
