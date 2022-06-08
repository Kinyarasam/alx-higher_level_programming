def best_score(a_dictionary):
    """Returns a key with the biggest integer value
    Args:
        a_dictionary: dictionary

    Returns:
        if no score is round, the return value is none
        otherwise, the biggest value
    """
    if a_dictionary:
        return max(a_dictionary, key = a_dictionary.get)
    return None
