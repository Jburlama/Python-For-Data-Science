from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class takes a first_name and a optional is_alive value"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        self.is_alive: bool = is_alive
        self.first_name: str = first_name


class Stark(Character):
    """docstring for class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """docstring for constroctor"""
        self.first_name = first_name
        super().__init__(first_name, is_alive)

    def die(self):
        """docstring for method"""
        self.is_alive = False
