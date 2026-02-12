class calculator:
    """Classe pour effectuer des opérations sur des vecteurs sans instance."""

    # zip(v1, v2) génère : (1.0, 10.0), (2.0, 20.0), (3.0, 30.0).
    def add_vec(V1: list, V2: list) -> None:
        """Ajoute le scalaire à chaque élément et affiche le vecteur."""
        res = [x + y for x, y in zip(V1, V2)]
        print(f"Add vector is : {res}")

    def dotproduct(V1: list, V2: list) -> None:
        """Multiplie le scalaire a chaque element et affiche le vecteur"""
        new_vec = [x * y for x, y in zip(V1, V2)]
        a = sum(new_vec)
        print(f"Dot product is : {a}")
    
    def sous_vec(V1: list, V2: list) -> None:
        """Multiplie le scalaire a chaque element et affiche le vecteur"""
        res = [x - y for x, y in zip(V1, V2)]
        print(f"Sous vector is : {res}")
