from abc import ABC, abstractmethod


class Character(ABC):
    """Doc string for abstract class"""
    def __init__(self, first_name: str, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def __dic__(self):
        return {"first_name": self.first_name, "is_alive": self.is_alive}

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Doc string for inherit class"""

    def __init__(self, first_name: str, is_alive=True):
        """Doc string for constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """turn is_alive from true to false"""
        self.is_alive = False
