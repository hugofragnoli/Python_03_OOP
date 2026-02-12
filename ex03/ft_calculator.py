class calculator:
    """Classe de base pour calculer."""
    def __init__(self, vector):
        """la classe se construit sur larray en param"""
        self.vec = vector

    def __add__(self, object) -> None:
        """Ajoute le scalaire à chaque élément et affiche le vecteur."""
        self.vec = [x + object for x in self.vec]
        print(self.vec)

    def __mul__(self, object) -> None:
        """Multiplie le scalaire a chaque element et affiche le vecteur"""
        self.vec = [x * object for x in self.vec]
        print(self.vec)
# def __sub__(self, object) -> None: #your code here
# def __truediv__(self, object) -> None: #your code here