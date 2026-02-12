class calculator:
    """Classe pour effectuer des opérations sur des vecteurs sans instance."""

    # zip(v1, v2) génère : (1.0, 10.0), (2.0, 20.0), (3.0, 30.0).
    def add_vec(self, object) -> None:
        """Ajoute le scalaire à chaque élément et affiche le vecteur."""
        self.vec = [x + y for x, y in zip(self.vec, object)]
        print(self.vec)

    def dotproduct(self, object) -> None:
        """Multiplie le scalaire a chaque element et affiche le vecteur"""
        new_vec = [x * y for x, y in zip(self.vec, object)]
        a = sum(new_vec)
        print(a)
    
    def sous_vec(self, object) -> None:
        """Multiplie le scalaire a chaque element et affiche le vecteur"""
        self.vec = [x - y for x, y in zip(self.vec, object)]
        print(self.vec)
