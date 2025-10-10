def callLimit(limit: int):
    """decorator to limit a function call"""
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count, limit

            if count < limit:
                function()
            else:
                print(f"Error: {function} call too many times")
            count += 1
            return function

        return limit_function

    return callLimiter
