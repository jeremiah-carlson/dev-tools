# Recursive binary search (array)
def binary_search_array(arr, val, base_index = 0):
    check = len(arr) // 2
    
    try:
        if arr[check] == val:
            return check + base_index
        else:
            if arr[check] < val:
                return binary_search_array(arr[check+1:], val, base_index=check+1)
            else:
                return binary_search_array(arr[:check], val, base_index)
    except IndexError:
        return -1