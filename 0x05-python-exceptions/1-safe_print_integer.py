#!/usr/bin/python3
def safe_print_integer(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list: list to print elements from
        x: The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    count = 0
    for numb in range(x):
        try:
            print("{:d}".format(my_list[numb]), end='')
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
