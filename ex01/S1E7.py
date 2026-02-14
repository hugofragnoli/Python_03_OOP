from S1E9 import Character


class Baratheon(Character):
    """This one is a Baratheon, look, how drunk he is no doubt about it..
    - How you doin' little deer  ?"""
    def __init__(self, first_name, is_alive=True):
        """
        Initialise un Baratheon avec son prénom et ses attributs par défaut.

        Args:
            first_name (str): Le prénom du Baratheon.
            is_alive (bool): Le statut de vie (True par défaut).

        Attributes:
            family_name (str): "Baratheon"
            eyes (str): "brown"
            hairs (str): "dark"
        """
        # super va chercher le __init__ de Character
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        Return une représentation sous forme de vecteur des traits de la famill
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Retourne la représentation technique de l'instance Baratheon.
        """
        return self.__str__()


class Lannister(Character):
    """This one is a Lannister, look, at his horrible blond hairs:
    no doubt about it..
    - How you doin' little Lion  ?"""
    def __init__(self, first_name, is_alive=True):
        """
        Initialise un Lannister avec son prénom et ses attributs par défaut.

        Args:
            first_name (str): Le prénom du Lannister.
            is_alive (bool): Le statut de vie (True par défaut).

        Attributes:
            family_name (str): "Lannister"
            eyes (str): "blue"
            hairs (str): "light"
        """
        # super va chercher le __init__ de Character
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        Return une représentation sous forme de vecteur des traits de la famill
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Retourne la représentation technique de l'instance Lannister.
        """
        return self.__str__()

    @classmethod
    def create_lannister(Lannister, first_name, is_alive=True):
        """
        Méthode de classe (Factory) pour créer une instance de Lannister.

        Args:
            first_name (str): Le prénom du Lannister.
            is_alive (bool): Le statut de vie (True par défaut).

        Returns:
            Lannister: Une nouvelle instance de la classe Lannister.
        """
        return Lannister(first_name, is_alive)
    pass
