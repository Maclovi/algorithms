def cache(func):
    cash = {}

    def wrapper(*args, **kwargs):
        nonlocal cash
        n = args[0]
        if n not in cash:
            cash[n] = func(*args, **kwargs)
        return cash[n]

    return wrapper


@cache
def fib(n):   # via recursion
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


@classmethod
def fib2(n):    # via cycle
    a, b = 0, 1
    for _ in range(n):
        a, b = b + a, a
    return a
