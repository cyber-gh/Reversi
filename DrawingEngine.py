import pygame
from helper import *
from GameState import *
from GameEngine import *
import math
import time

GREEN = (50, 168, 82)
DARK_GREEN = (3, 44, 10)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BLUE = (44, 44, 255)

pygame.init()


class DrawingEngine:

    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

    def draw_board(self):
        config = self.game_engine.state.config
        moves = list(self.game_engine.state.possible_moves())
        for i in range(1, len(config)):
            for j in range(1, len(config)):
                pygame.draw.rect(self.screen, GREEN, ((i - 1) * SQUARE_SIZE, (j - 1) * SQUARE_SIZE, 100, 100))
                pygame.draw.rect(self.screen, DARK_GREEN, ((i - 1) * SQUARE_SIZE, (j - 1) * SQUARE_SIZE, 100, 100),
                                 width=2)
                curr_color = BLACK if self.game_engine.state.current_player == JMAX else WHITE
                if (i, j) in moves:
                    pygame.draw.circle(self.screen, curr_color,((i - 1) * SQUARE_SIZE + SQUARE_SIZE / 2, (j - 1) * SQUARE_SIZE + SQUARE_SIZE / 2),
                                   SQUARE_SIZE / 2 - 10, width=2)
                if config[i][j] == EMPTY:
                    continue
                color = BLACK if config[i][j] == JMAX else WHITE
                pygame.draw.circle(self.screen, color,
                                   ((i - 1) * SQUARE_SIZE + SQUARE_SIZE / 2, (j - 1) * SQUARE_SIZE + SQUARE_SIZE / 2),
                                   SQUARE_SIZE / 2 - 10)



    def run(self):
        running = True
        counter = 1
        skip_frames = 60
        while running:
            if counter > 100000:
                counter = 0
            player = "Black" if self.game_engine.state.current_player == JMAX else "White"
            player += " moves"
            pygame.display.set_caption(player)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_engine.state.current_player != self.game_engine.human:
                        continue
                    x, y = pygame.mouse.get_pos()
                    x /= SQUARE_SIZE
                    y /= SQUARE_SIZE
                    x = int(math.floor(x)) + 1
                    y = int(math.floor(y)) + 1
                    try:
                        self.game_engine.player_move_to_pos(x, y)
                    except Exception as e:
                        print("Unable to move ", e)

            self.game_engine.check_not_stuck()

            if self.game_engine.state.is_final():
                print("Reached game over")
                font = pygame.font.Font('freesansbold.ttf', 50)
                text = font.render("Game over: Winner is {}".format(self.game_engine.state.winner()), True, GREEN, BLUE)
                X, Y = SCREEN_SIZE
                self.screen.blit(text, (SQUARE_SIZE // 2, Y // 2))
                pygame.display.update()
                continue

            if counter % skip_frames == 0 and self.game_engine.state.current_player == self.game_engine.computer:
                self.game_engine.ai_move()
            # if self.game_engine.state.current_player == self.game_engine.human:
            #     self.game_engine.random_move()



            self.draw_board()
            pygame.display.update()
            counter += 1


if __name__ == '__main__':
    while True:
        try:
            human = input("Alb sau negru (w/b)?")
            assert human == JMIN or human == JMAX
            break
        except AssertionError as e:
            print("Invalid choice, try again")

    while True:
        try:
            algorithm = int(input("Minimax sau alpha-beta(1/2)?"))
            assert algorithm == 1 or algorithm == 2
            break
        except AssertionError as e:
            print("Invalid choice, try again")

    drawing_engine = DrawingEngine(GameEngine(GameState(),human=human, algorithm=algorithm))
    drawing_engine.run()
