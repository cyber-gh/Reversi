from helper import *
from GameState import *
import time
from func_timeout import func_timeout, FunctionTimedOut


class GameEngine:

    MAX_DEPTH = 7
    TIMEOUT = 3

    def __init__(self, state, human=JMIN, algorithm=1):
        self.algorithm = algorithm
        assert algorithm == 1 or algorithm == 2
        self.human = human
        assert human == JMIN or human == JMAX
        self.computer = JMAX if human == JMIN else JMIN
        self.state = state


    @staticmethod
    def alpha_beta(state, depth, alpha, beta):
        if depth == 0 or state.is_final():
            return state, state.score()

        if state.current_player == JMAX:
            maxEval = -1e9
            picked_state = None
            for child in state.next_states():
                move, score = GameEngine.alpha_beta(child, depth - 1, alpha, beta)
                if score > maxEval:
                    maxEval = score
                    picked_state = child

                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return picked_state, maxEval
        if state.current_player == JMIN:
            minEval = 1e9
            picked_state = None
            for child in state.next_states():
                move, score = GameEngine.alpha_beta(child, depth - 1, alpha, beta)
                if score < minEval:
                    minEval = score
                    picked_state = child
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return picked_state, minEval

    @staticmethod
    def mini_max(state, depth):
        if depth == 0 or state.is_final():
            return state, state.score()

        if state.current_player == JMAX:
            maxEval = -1e9
            picked_state = None
            for child in list(state.next_states()):
                nxt, score = GameEngine.mini_max(child, depth - 1)
                if score > maxEval:
                    maxEval = score
                    picked_state = child
            return picked_state, maxEval
        if state.current_player == JMIN:
            minEval = 1e9
            picked_state = None
            for child in list(state.next_states()):
                nxt, score = GameEngine.mini_max(child, depth - 1)
                if score < minEval:
                    minEval = score
                    picked_state = child
            return picked_state, minEval


    def player_move(self):
        print(self.state)
        while True:
            try:
                if self.state.must_skip_turn():
                    print("You have nowhere to move, skipping your turn...")
                inp = input("Your move: ").split(" ")
                x = int(inp[0])
                y = int(inp[1])
                self.player_move_to_pos(x, y)
                break
            except Exception as e:
                print("Error, try again", e)

    def player_move_to_pos(self, x, y):
        nxt = self.state.next_state_by_moving_to(x, y)
        self.state = nxt

    def incremental_mini_max(self):
        move, score = GameEngine.mini_max(self.state, 1)
        d = 1
        for depth in range(2, GameEngine.MAX_DEPTH  + 1):
            try:
                d = depth
                move, score = func_timeout(GameEngine.TIMEOUT, GameEngine.mini_max, args=(self.state, depth))
            except FunctionTimedOut:
                break
        return move, score, d

    def incremental_alpha_beta(self):
        move, score = GameEngine.alpha_beta(self.state, 1, -1e9, 1e9)
        d = 1
        for depth in range(2, GameEngine.MAX_DEPTH  + 1):
            try:
                d = depth
                move, score = func_timeout(GameEngine.TIMEOUT, GameEngine.alpha_beta, args=(self.state, depth, -1e9, 1e9))
            except FunctionTimedOut:
                break
        return move, score, d

    def ai_move(self):
        print("AI turn")
        print(self.state)
        if self.state.must_skip_turn():
            self.state.flip_player()
            return
        st = time.time()
        # move, score = GameEngine.mini_max(self.state, GameEngine.MAX_DEPTH)
        move, score, depth = self.incremental_mini_max() if self.algorithm == 1 else self.incremental_alpha_beta()
        time_elapsed = time.time() - st
        print("Picked state with score {}\n Time elapsed: {}\n Reached depth: {}".format(score, time_elapsed, depth))
        self.state = move

    def check_not_stuck(self):
        if self.state.must_skip_turn():
            self.state.flip_player()

    def start(self):
        print("Game started")
        while not self.state.is_final():
            self.ai_move()
            self.player_move()
        print(self.state)


if __name__ == '__main__':
    engine = GameEngine(GameState())
    engine.start()
