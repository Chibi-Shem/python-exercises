

def remove_duplicate(lst):
    """Removes duplicate objects in lst."""

    new_list=[]
    for x in range(len(lst)):
    	if new_list.count(lst[x])<1:
	    	new_list.append(lst[x])
    return new_list


print(remove_duplicate([1, 2, 3, 4, 1, 2]))
