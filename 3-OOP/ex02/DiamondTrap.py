from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Numa classe neto, python usa o algoritimo de linearização C3 para
    evitar o problema de diamante"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Se ambos Baretheon e Lannister compartilham uma propriedade, o
        mais a esquerda vai ter precedencia"""
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
