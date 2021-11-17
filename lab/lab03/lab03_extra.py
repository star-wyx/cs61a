""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def aim():
        return n

    def recursion(i):
        if i == 1:
            return True
        if aim() % i == 0:
            return False
        else:
            return recursion(i-1)

    return recursion(n-1)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a % b == 1:
        return 1
    if a % b == 0:
        return b
    return gcd(b,a%b)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    num = [0,0,0,0,0,0,0,0,0,0]

    def recursion(x):
        if x<10:
            num[x] += 1
            return
        tmp = x % 10
        num[tmp] += 1
        recursion(x//10)

    recursion(n)
    return num[1]*num[9]+num[2]*num[8]+num[3]*num[7]+num[4]*num[6]+num[5]*(num[5]-1)//2
