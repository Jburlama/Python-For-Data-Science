def square(x: int | float) -> int | float:
    """Return the square of x """
    return x * x


def pow(x: int | float) -> int | float:
    """Return the square root of x """
    return x ** x


def outer(x: int | float, function) -> object:
    """decorator for function"""
    count = 0

    def inner() -> float:
        """uses nonlocal to retain the value of use count and x in inner scope
        and retain the value on multiple calls"""
        nonlocal count, x

        res = function(x)
        x = res
        return res

    return inner
