from helper import *
from copy import deepcopy as dp
from random import choice


class GameState:

    def __str__(self):
        tmp = ""
        if self.is_final():
            tmp += "Game over\n Winner is " + self.winner() + "\n"
        else:
            tmp += "{} turn's\n".format(self.current_player)
        for line in self.config[1:]:
            tmp += " ".join(line[1:]) + "\n"
        return tmp

    def __eq__(self, other):
        return all(self.config[i] == other.config[i] for i in range(0, self.n)) \
               and self.current_player == other.current_player and self.n == other.n

    def __hash__(self):
        return hash(tuple(tuple(x) for x in self.config) + tuple(self.current_player))

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
        pieces = self.get_all_pieces()
        for x, y in pieces:
            for move in self.possible_move_from(x, y):
                yield move

    def possible_moves_with_sources(self):
        pieces = self.get_all_pieces()
        for x, y in pieces:
            for to_x, to_y in self.possible_move_from(x, y):
                yield to_x, to_y, x, y

    def next_state_by_moving_to(self, x, y):
        nxt = dp(self)
        if not (x, y) in self.possible_moves() or not self.in_range(x, y):
            raise ValueError("Can't move here {}, {}".format(x, y))
        for to_x, to_y, from_x, from_y in self.possible_moves_with_sources():
            if (to_x, to_y) == (x, y):
                dx = (to_x - from_x) // (abs(to_x - from_x) if abs(to_x - from_x) > 0 else 1)
                dy = (to_y - from_y) // (abs(to_y - from_y) if abs(to_y - from_y) > 0 else 1)
                curr_x, curr_y = from_x, from_y
                while (curr_x, curr_y) != (to_x, to_y):
                    nxt.config[curr_x][curr_y] = nxt.current_player
                    curr_x += dx
                    curr_y += dy
        nxt.config[x][y] = nxt.current_player
        nxt.flip_player()
        return nxt

    def random_move(self):
        if self.must_skip_turn():
            return None
        return choice(self.next_states())

    def board_is_full(self):
        return sum(sum(1 if x == EMPTY else 0 for x in line) for line in self.config) == 0

    def must_skip_turn(self):
        if len(list(self.possible_moves())) == 0:
            return True
        return False

    def is_final(self):
        nxt = dp(self)
        nxt.flip_player()
        return self.board_is_full() or (self.must_skip_turn() and nxt.must_skip_turn())

    def nr_pieces_of(self, player):
        return sum(sum(1 if x == player else 0 for x in line) for line in self.config)

    def winner(self):
        if not self.is_final():
            return None
        jmax = self.nr_pieces_of(JMAX)
        jmin = self.nr_pieces_of(JMIN)
        if jmax == jmin:
            return "TIE"
        return JMAX if jmax > jmin else JMIN

    def next_player(self):
        return JMAX if self.current_player == JMIN else JMIN

    def flip_player(self):
        self.current_player = self.next_player()

    def score(self):
        winner = self.winner()
        if winner == JMAX:
            return MAX_SCORE
        elif winner == JMIN:
            return -MAX_SCORE
        elif winner == "TIE":
            return 0
        return self.nr_pieces_of(JMAX)

    def next_states(self):
        states = []
        for x, y in self.possible_moves():
            states.append(self.next_state_by_moving_to(x, y))
        return states


if __name__ == '__main__':
    print(GameState())
