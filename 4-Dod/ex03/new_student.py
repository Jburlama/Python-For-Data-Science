import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate random id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class the filds login and id will be created after construct"""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
        self.id = generate_id()
