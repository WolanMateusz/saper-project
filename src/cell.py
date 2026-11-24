class Cell:
    def __init__(self, is_mine: bool = False):
        # Podstawowe cechy pola
        self.is_mine = is_mine          # Czy na polu jest mina (True/False)
        self.is_revealed = False        # Czy pole zostało już odkryte przez gracza
        self.is_flagged = False         # Czy pole zostało oznaczone flagą
        self.neighbor_mines = 0         # Liczba min w bezpośrednim sąsiedztwie

    def reveal(self):
        """Odkrywa pole, ale tylko wtedy, gdy nie ma na nim flagi."""
        if not self.is_flagged:
            self.is_revealed = True

    def toggle_flag(self):
        """Oznacza pole flagą lub ją zdejmuje, o ile pole nie zostało odkryte."""
        if not self.is_revealed:
            self.is_flagged = not self.is_flagged
