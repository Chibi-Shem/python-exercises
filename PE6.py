

def check_empty_list(lst):
    """Checks if lst is empty."""

    if not lst:
        return 'List is empty.'
    else:
        return 'List is not empty.'


lst = []
print(check_empty_list(lst))
