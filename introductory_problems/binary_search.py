

def find_first_occurence(arr, element):
    st = 0
    en = len(arr) - 1

    while st < en:
        mid = st + (en-st)//2
        if arr[mid] >= element:
            if arr[mid - 1] < element:
                return mid
            en = mid - 1
        else:
            st = mid + 1

    return st if arr[st] >= element else -1


def find_last_occurence(arr, element):
    st = 0
    en = len(arr) - 1
    
    while st < en:
        mid = st + (en - st)//2
        
        if arr[mid] <= element:
            if arr[mid + 1] > element:
                return mid
            st = mid + 1
        else:
            en = mid - 1
    return st if arr[st] <= element else -1

