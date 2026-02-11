from abc import ABC, abstractmethod

class Character(ABC):
    """
    Docstring pour Character
    """
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def __str__(self):
        # ici on met rien, on dit a python : je vais donner cette methode
        # a toutes les classes qui heriteront de celle la (abstr).
        pass

    def __repr__(self):
        # repr est destinee au dev. Elle doit etre technique
        # et permettre de reconstruire lobjet.
        # utilisee quand on tape le nom la variable dans la
        # console ou quand on affiche une liste dobjets.
        pass


class Stark(Character):
    """
    Docstring pour Stark
    """

