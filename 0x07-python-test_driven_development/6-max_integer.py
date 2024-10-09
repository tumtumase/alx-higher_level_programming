def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers.
       If the list is empty, the function returns None.
       Raises TypeError if the input is not a list.
    """
    if not isinstance(list, list):
        raise TypeError("Input must be a list")
    
    if len(list) == 0:
        return None

    result = list[0]
    for i in range(1, len(list)):
        if list[i] > result:
            result = list[i]
    return result
