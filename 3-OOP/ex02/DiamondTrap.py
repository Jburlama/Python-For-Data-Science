from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Grand Child class, python uses the C3 linearization algorithm
    to aviod the diamond problem"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """If both Baratheon and Lannister share a property
        the most left will take precedence"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        """Seter for the eyes"""
        self.eyes = color

    def get_eyes(self):
        """Geter for the eyes"""
        return self.eyes

    def set_hairs(self, hair: str):
        """Seter for the hairs"""
        self.hairs = hair

    def get_hairs(self):
        """Geter for the hairs"""
        return self.hairs
