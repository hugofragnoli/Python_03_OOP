from S1E9 import Character

class Baratheon(Character):
    """This one is a Baratheon, look, how drunk he is no doubt about it..
    - How you doin' little deer  ?"""
    def __init__(self, first_name, is_alive=True):
        """Initialise un Baratheon avec ses attributs physiques par défaut."""
        # super va chercher le __init__ de Character
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    def __repr__(self):
        return self.__str__()

class Lannister(Character):
    """This one is a Lannister, look, at his horrible blond hairs: no doubt about it..
    - How you doin' little Lion  ?"""
    def __init__(self, first_name, is_alive=True):
        """Initialise un Lannister avec ses attributs physiques par défaut."""
        # super va chercher le __init__ de Character
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_lannister(Lannister, first_name, is_alive=True):
        """Méthode de classe pour créer un Lannister."""
        return Lannister(first_name, is_alive)
    pass