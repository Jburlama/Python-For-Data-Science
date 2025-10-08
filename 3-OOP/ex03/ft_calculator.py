class calculator:
    """Vector calculator"""
    def __init__(self, vec: list[float]):
        """Inicialize by taking a list of floats"""
        self.vec = vec

    def __add__(self, object) -> None:
        """perform adition"""
        self.vec = [i + object for i in self.vec]
        print(self.vec)

    def __mul__(self, object) -> None:
        """perform multiplication"""
        self.vec = [i * object for i in self.vec]
        print(self.vec)

    def __sub__(self, object) -> None:
        """perform subtraction"""
        self.vec = [i - object for i in self.vec]
        print(self.vec)

    def __truediv__(self, object) -> None:
        """perform division"""
        try:
            self.vec = [i / object for i in self.vec]
            print(self.vec)
        except ZeroDivisionError:
            print("Cannot divide by zero!")
