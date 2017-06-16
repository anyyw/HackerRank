def twinArrays(ar1, ar2):
    #Iterate through each array, find the minimum and next minimum
    #If minumim for both arrays have the same index, cross compare the two next min
    first1 = min(ar1)
    first2 = min(ar2)
    second1 = max(ar1)
    second2 = max(ar2)
    
    for c in ar1:
        if (c < second1) and (c != first1):
            second1 = c
    for d in ar2:
        if (d < second2) and (d != first2):
            second2 = d
        
    indices1 = [i for i, x in enumerate(ar1) if x == first1]
    indices2 = [i for i, x in enumerate(ar2) if x == first2]

    if (ar1.index(first1) != ar2.index(first2)) or ((len(indices1) != 1) or (len(indices2) != 1)):
        return first1 + first2
    else:
        secondmin1 = first1 + second2
        secondmin2 = first2 + second1
        return secondmin1 if (secondmin1 < secondmin2) else secondmin2