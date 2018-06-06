

def check_empty_list(lst):
    """Checks if lst is empty."""

    if(len(lst) == 0):
        return 'List is empty.'
    else:
        return 'List is not empty.'


lst = []
print(check_empty_list(lst))
