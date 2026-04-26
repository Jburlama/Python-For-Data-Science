"""
A função `filter()` é uma função de ordem integrada que retorna um
iterador a partir de elementos de um iterável para os quais uma
função retorna `true`.

```
numbers = [1, 2, 3, 4, 5, 6]

def is_even(n):
    return n % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

Os iteradores são objetos que permitem percorrer todos os elementos de uma
coleção, independente de sua implementação específica.

Os iteradores são objetos que implementam o protocolo de iteradores.
contem os métodos __iter__()  e __next__().
"""


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
