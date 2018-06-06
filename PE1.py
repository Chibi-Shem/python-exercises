

def dict_persons(persons):
    """Groups the list persons in two groups and
    returns a dictionary of grouped persons.
    """

    grouped_dict = {}
    grouped_dict.update({'A': persons[:len(persons)/2]})
    grouped_dict.update({'B': persons[len(persons)/2:]})
    return grouped_dict


lst=['Shem', 'JC', 'Joshua', 'Arriane', 'John Smith']
print(dict_persons(lst))
