# CPE 202 Lab 1
# Stefan Patch

def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == []:
        return None
    elif int_list == None:
        raise ValueError
    else:
        max_val = int_list[0]
        for i in int_list:
            if i > max_val:
                max_val = i
        return max_val


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError
    elif len(int_list) <= 1:
        return int_list
    return reverse_rec(int_list[1:]) + int_list[:1]

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list == None:
        raise ValueError
    if low > high:
        return None
    half = ((high - low) // 2) + low
    if int_list[half] == target:
        return half
    elif int_list[half] > target:
        return bin_search(target, low, half - 1, int_list)
    else:
        return bin_search(target, half + 1, high, int_list)
