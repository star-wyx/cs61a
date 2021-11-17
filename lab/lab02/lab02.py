"""Lab 2: Lambda Expressions and Higher Order Functions"""


# Lambda Functions

def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    "*** YOUR CODE HERE ***"

    def curried_add(f):
        def first(x):
            def second(y):
                return f(x, y)

            return second

        return first

    return curried_add(func)
