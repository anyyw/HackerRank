def patternCount(s):
    #Hacked as balls
    count = 0
    sp = s.split("1")
    for a in sp:
        try:
            b = int(a)
        except ValueError:
            continue
        if (b == 0) and (sp[-1] != a):
            count += 1
    return count