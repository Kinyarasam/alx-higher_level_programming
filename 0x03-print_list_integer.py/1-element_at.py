#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a linked list
    """
    if (idx < 0 and idx > len(my_list) - 1):
        return None
    else:
        return my_list[idx]
