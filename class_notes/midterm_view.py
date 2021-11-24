def count_groupings(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    res = 0
    for i in range(1, n):
        res += count_groupings(i) * count_groupings(n - i)
    return res
