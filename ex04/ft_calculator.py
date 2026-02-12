class calculator:
    """Classe de base pour calculer."""
    def __init__(self, vector):
        """la classe se construit sur larray en param"""
        self.vec = vector

    # zip(v1, v2) génère : (1.0, 10.0), (2.0, 20.0), (3.0, 30.0).
    def __add_vec__(self, object) -> None:
        """Ajoute le scalaire à chaque élément et affiche le vecteur."""
        self.vec = [x + y for x, y in zip(self.vec, object)]
        print(self.vec)

    def __dotproduct__(self, object) -> None:
        """Multiplie le scalaire a chaque element et affiche le vecteur"""
        self.vec = [x * y for x, y in zip(self.vec, object)]
        a = sum(self.vec)
        print(a)
    
    def __sous_vec__(self, object) -> None:
        """Multiplie le scalaire a chaque element et affiche le vecteur"""
        self.vec = [x - y for x, y in zip(self.vec, object)]
        print(self.vec)
