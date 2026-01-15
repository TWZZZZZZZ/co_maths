import matplotlib.pyplot as plt

class Espace_lineaire:
    def __init__(self, a, b, n):
        # Initialisation des attributs
        self.a = a
        self.b = b
        self.n = n
        self.abscisses = []
        self.ordonnees = []
        # Calcul initial des abscisses
        self.calcule_abscisses()

    def calcule_abscisses(self):
        """Recalcule la liste des abscisses en fonction de a, b et n"""
        self.abscisses = []
        if self.n > 1:
            delta = (self.b - self.a) / (self.n - 1)
            for i in range(self.n):
                self.abscisses.append(self.a + i * delta)
        else:
            self.abscisses = [self.a]

    # --- Accesseurs (Getters) ---
    def get_a(self): return self.a
    def get_b(self): return self.b
    def get_n(self): return self.n
    def get_abscisses(self): return self.abscisses
    def get_ordonnees(self): return self.ordonnees

    # --- Mutateurs (Setters) ---
    def set_a(self, nouvelle_valeur):
        self.a = nouvelle_valeur
        self.calcule_abscisses() # Important : on recalcule !

    def set_b(self, nouvelle_valeur):
        self.b = nouvelle_valeur
        self.calcule_abscisses()

    def set_n(self, nouvelle_valeur):
        if nouvelle_valeur > 1:
            self.n = nouvelle_valeur
            self.calcule_abscisses()

    # --- Méthodes d'affichage (Partie 3) ---
    
    def set_ordonnees(self, f):
        """Calcule les images de chaque abscisse par la fonction f"""
        self.ordonnees = []
        for x in self.abscisses:
            self.ordonnees.append(f(x))

    def trace(self):
        """Ajoute la courbe au graphique actuel"""
        if len(self.abscisses) == len(self.ordonnees):
            plt.plot(self.abscisses, self.ordonnees, label=f"n={self.n}")
            plt.grid(True)
            plt.legend()

    def show(self):
        """Affiche la fenêtre matplotlib"""
        plt.show()

# --- f) Tests ---
if __name__ == "__main__":
    # Création d'un objet [5, 6] avec 5 points
    test = Espace_lineaire(5, 6, 5)
    print(f"Abscisses initiales : {test.get_abscisses()}")
    
    # Test des mutateurs
    test.set_a(0)
    test.set_b(10)
    test.set_n(11)
    print(f"Nouvelles abscisses (0 à 10, 11 pts) : {test.get_abscisses()}")