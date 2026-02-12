from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """This one is a King, half Lannister half Baratheon...
    - How you doin' little Joffrey  ?"""
    def __init__(self, first_name, is_alive=True):
        """Initialise un King avec ses attributs physiques par défaut."""
        # super va chercher le __init__ de Character
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    def set_eyes(self, color):
        """Change la couleur des yeux du roi."""
        self.eyes = color

    def set_hairs(self, color):
        """Change la couleur des cheveux du roi."""
        self.hairs = color

    def get_eyes(self):
        """Retourne la couleur des yeux du roi."""
        return self.eyes

    def get_hairs(self):
        """Retourne la couleur des cheveux du roi."""
        return self.hairs
