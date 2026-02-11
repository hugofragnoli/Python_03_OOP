from abc import ABC, abstractmethod

class Character(ABC):
    """
    Docstring pour Character
    """
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(Character):
    """
    Docstring pour Stark
    """
    
