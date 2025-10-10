class calculator:
    """Caltuculator uses staticmethod decorators to use the method without
        intantialize the object"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates the dot product of two vectors"""
        v = [i * j for i, j in zip(V1, V2)]

        dot = 0
        for i in v:
            dot += i
        print(f"Dot product is: {dot}")
        return

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates the sum of two vectors"""
        v = [i + j * 1.0 for i, j in zip(V1, V2)]
        print(f"Add Vector is : {v}")
        return

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates the subtraction of two vectors"""
        v = [i - j * 1.0 for i, j in zip(V1, V2)]
        print(f"Sous Vector: {v}")
        return
