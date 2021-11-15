def cont_up(n):
    if n == 1:
        print(n)
    else:
        cont_up(n - 1)
        print(n)
    return


def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


def cascade(n):
    print(n)
    if n > 10:
        cascade(n // 10)
        print(n)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def count_partitions(n, m):
    if n < m:
        return count_partitions(n, n)
    if m == 0:
        return 1
    elif m == 1:
        return 1
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)


def count_partitions_answer(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions_answer(n - m, m) + count_partitions_answer(n, m - 1)


print(count_partitions_answer(10, 8))
print(count_partitions(10, 8))
# print(fibonacci(30))
# cascade(486)
# cont_up(5)
# print(sum_digits(2088))
