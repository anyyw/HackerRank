def get(n):
    if n < 2:
        return n
    return get(n-2) + get(n-1)