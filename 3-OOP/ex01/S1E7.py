from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    @property
    def __str__(self):
        return f"""\
<bound method Baratheon.__str__ of Vector:\
('{self.family_name}', '{self.eyes}', '{self.hairs}')"""

    @property
    def __repr__(self):
        return f"""\
<bound method Baratheon.__repr__ of Vector:\
('{self.family_name}', '{self.eyes}', '{self.hairs}')"""

    def die(self):
        self.is_alive = False

    @staticmethod
    def create_baratheon(first_name: str, is_alive: bool = True):
        return Lannister(first_name, is_alive)


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @property
    def __str__(self):
        return f"""\
<bound method Lannister.__str__ of Vector:\
('{self.family_name}', '{self.eyes}', '{self.hairs}')"""

    @property
    def __repr__(self):
        return f"""\
<bound method Lannister.__repr__ of Vector:\
('{self.family_name}', '{self.eyes}', '{self.hairs}')"""

    def die(self):
        self.is_alive = False

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True):
        return Lannister(first_name, is_alive)
