def fib():
    i = 0
    prev = 0
    curr = 1
    while i < 10:
        i = i + 1
        print(prev)
        tmp = curr
        curr = curr + prev
        prev = tmp

fib()