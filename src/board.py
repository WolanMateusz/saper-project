import random
from src.cell import Cell


class Board:
    def __init__(self, rows: int, cols: int, mines_count: int):
        self.rows = rows                  # Liczba wierszy
        self.cols = cols                  # Liczba kolumn
        self.mines_count = mines_count    # Liczba min na planszy
        self.game_over = False            # Czy gracz trafil na mine
        self.victory = False              # Czy gracz odkryl wszystkie bezpieczne pola

        # Tworzenie siatki pol
        self.grid = [
            [Cell(is_mine=False) for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

        # Losujemy miny i liczymy sasiadow po starcie planszy (te funkcje sa do wykanania przy kolejnej sesji pracy nad projektem!!!)
        self._place_mines()
        self._calculate_neighbors()