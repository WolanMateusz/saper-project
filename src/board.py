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

        # Losujemy miny i liczymy sasiadow po starcie planszy
        self._place_mines()
        self._calculate_neighbors()

        def is_inside(self, row: int, col: int) -> bool:     # Czy wspolzedne mieszcza sie na planszy
            return 0 <= row < self.rows and 0 <= col < self.cols

    def _place_mines(self):  # Losuje miny na planszy po wlaczeniu gry
        placed = 0
        while placed < self.mines_count:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)

            if not self.grid[r][c].is_mine:
                self.grid[r][c].is_mine = True
                placed += 1

    def _calculate_neighbors(self):    # Liczy ile jest min w sasiednich polach
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c].is_mine:
                    continue

                mine_neighbors = 0
                # Przegladamy 8 sasiednich pol
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue

                        nr, nc = r + dr, c + dc
                        if self.is_inside(nr, nc) and self.grid[nr][nc].is_mine:
                            mine_neighbors += 1

                self.grid[r][c].neighbor_mines = mine_neighbors