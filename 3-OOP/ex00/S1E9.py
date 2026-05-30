from abc import ABC, abstractmethod


class Character(ABC):
    """Quando uma class herda da class ABS ela se tornar um molde para
    outras classes, Não permitindo instanciar Character
"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """O decorador @abstractmethod faz com que todos os metodos definidos
        no constructor passam a ser obrigatorios nas classes quer herdarem de
        Character
"""
        self.is_alive: bool = is_alive
        self.first_name: str = first_name


class Stark(Character):
    """docstring for class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """O metodo super() instancia os metodos da classe devinidas nas
        classe mãe
"""
        super().__init__(first_name, is_alive)

    def die(self):
        """docstring for method"""
        self.is_alive = False
