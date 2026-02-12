from abc import ABC, abstractmethod


class Character(ABC):
    """
    Classe de base abstraite pour tous les personnages.
    Elle définit le contrat que chaque famille doit suivre.
    """
    def __init__(self, first_name, is_alive=True):
        """Every class that inherits from Char Will have a first name and
        a bool to determine if she/he's alive"""
        self.first_name = first_name
        self.is_alive = is_alive

    # le decorateur @abstractmethod oblige les classes enfant
    # a devoir partager cette methode. Sinon linterpreteur ping
    # ici on met rien, on dit a python : je vais donner cette methode
    # a toutes les classes qui heriteront de celle la (abstr).
    @abstractmethod
    def __str__(self):
        pass

    # repr est destinee au dev. Elle doit etre technique
    # et permettre de reconstruire lobjet.
    # utilisee quand on tape le nom la variable dans la
    # console ou quand on affiche une liste dobjets.
    @abstractmethod
    def __repr__(self):
        pass

    def die(self):
        """Tue le Character en changeant son état"""
        self.is_alive = False


class Stark(Character):
    """
    This one is a Stark from Winterfell, no doubt about it..
    - How you doin' little wolf ?
    """
    def __init__(self, first_name, is_alive=True):
        """Initialise un Stark avec ses attributs physiques par défaut."""
        # super va chercher le __init__ de Character
        super().__init__(first_name, is_alive)

    def __str__(self):
        return f"('{self.first_name}', '{self.is_alive}')"
    def __repr__(self):
        return self.__str__()
