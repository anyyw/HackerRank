def sort(unsorted):
    if (len(unsorted) is 0) or (len(unsorted) is 1):
        return unsorted
    first = unsorted[0:len(unsorted)/2]
    second = unsorted[len(unsorted)/2:-1]
    print second