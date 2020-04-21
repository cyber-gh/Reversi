from helper import *
from GameState import *


class GameEngine:

    def __init__(self, state):
        self.state = state

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

    def ai_move(self):
        print("AI turn")
        print(self.state)
        move = self.state.random_move()
        if move is not None:
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
