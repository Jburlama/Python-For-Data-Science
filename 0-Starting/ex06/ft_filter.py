class ft_filter:
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    def __init__(self, function, iterable):
        self.function = function
        self.iter = iter(iterable)

    def __iter__(self):
        """Makes the class a iterable object"""
        return self

    def __next__(self):
        if (self.function):
            self.iter = iter([i for i in self.iter if self.function(i)])
        return next(self.iter)

    def __repr__(self):
        """Change the description of the class"""
        return f"<ft_filter object at {hex(id(self))}>"
