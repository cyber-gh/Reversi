from helper import *
from copy import deepcopy as dp


class GameState:

    def __eq__(self, other):
        return all(self.config[i] == other.config[i] for i in range(0, self.n)) \
               and self.current_player == other.current_player and self.n == other.n

    def __init__(self, config=INITIAL_CONFIG, current_player=JMAX):
        self.current_player = current_player
        self.config = dp(config)
        self.n = len(self.config) - 1

    def get_all_pieces(self):
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                if self.config[i][j] == self.current_player:
                    yield i, j

    def in_range(self, x, y):
        return 1 <= x <= self.n and 1 <= y <= self.n

    def possible_move_from_direction(self, curr_x, curr_y, dx, dy):
        if self.config[curr_x + dx][curr_y + dy] == self.next_player():
            curr_x += dx
            curr_y += dy
            while self.in_range(curr_x, curr_y) and self.config[curr_x][curr_y] == self.next_player():
                curr_x += dx
                curr_y += dy
            if self.in_range(curr_x, curr_y) and self.config[curr_x][curr_y] == EMPTY:
                return curr_x, curr_y
            else:
                return None
        else:
            return None

    def possible_move_from(self, x, y):
        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [1, 1, 0, -1, -1, -1, 0, 1]
        for dirx, diry in zip(dx, dy):
            move = self.possible_move_from_direction(x, y, dirx, diry)
            if move is not None:
                yield move

    def possible_moves(self):
        return []

    def is_final(self):
        return True

    def winner(self):
        return None

    def next_player(self):
        return JMAX if self.current_player == JMIN else JMIN

    def score(self):
        return 0

    def next_states(self):
        return []
