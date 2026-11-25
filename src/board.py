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

    def reveal_cell(self, row: int, col: int):  #Funkcja odkrywajaca pole
        if not self.is_inside(row, col) or self.game_over or self.victory:
            return

        cell = self.grid[row][col]

        #Sprawdzamy czy pole nie jest juz odkryte lub oflagowane
        if cell.is_revealed or cell.is_flagged:
            return

        cell.reveal()

        #Trafienie w mine to przegrana
        if cell.is_mine:
            self.game_over = True
            return

        #Jesli pole nie ma zadnej miny obok, odslaniamy sasiednie pola
        if cell.neighbor_mines == 0:
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    self.reveal_cell(row + dr, col + dc)

        self._check_victory()

    def toggle_flag(self, row: int, col: int):   #Stawia lub zdejmuje flage na wybranym polu
        if not self.is_inside(row, col) or self.game_over or self.victory:
            return

        self.grid[row][col].toggle_flag()

    def _check_victory(self):   #Sprawdza czy wszystkie pola nie bedace minami zostaly odkryte
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                if not cell.is_mine and not cell.is_revealed:
                    return

        self.victory = True