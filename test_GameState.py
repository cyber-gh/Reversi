from unittest import TestCase
from unittest import skip
from GameState import *
from helper import *


class TestGameState(TestCase):

    def setUp(self) -> None:
        self.state = GameState()

    def test_invalid_move(self):
        try:
            state = GameState().next_state_by_moving_to(1, 1)
            assert False
        except ValueError as e:
            assert True

    def test_board_is_full(self):
        state = GameState(FINAL_CONFIG)
        assert state.board_is_full() == True

    def test_is_final(self):
        state = GameState(FINAL_CONFIG)
        assert state.is_final() == True

    def test_winner(self):
        state = GameState(FINAL_CONFIG)
        assert state.winner() == JMAX

    def test_score_jmax_won(self):
        state = GameState(FINAL_CONFIG)
        score = state.score()
        correct_score = MAX_SCORE
        return score == correct_score

    def test_score_initial(self):
        state = GameState()
        score = state.score()
        correct_score = 2
        return score == correct_score

    def test_next_player(self):
        state = GameState(current_player=JMAX)
        assert state.next_player() == JMIN

        state = GameState(current_player=JMIN)
        assert state.next_player() == JMAX



    def test_possible_moves_from(self):
        state = GameState()
        moves = list(state.possible_move_from(4, 4))
        correct_moves = [(6, 4), (4, 6)]
        assert set(moves) == set(correct_moves)

    def test_possible_move_from_with_2_boundary(self):
        state = GameState()
        other = state.next_player()
        state.config[4][1] = other
        state.config[4][2] = other
        state.config[4][3] = other
        state.config[4][6] = other
        state.config[4][7] = other
        state.config[4][8] = other

        moves = list(state.possible_move_from(4, 4))
        correct_moves = [(6, 4)]
        return set(moves) == set(correct_moves)

    def test_possible_move_from_with_1_boundary(self):
        state = GameState()
        other = state.next_player()
        state.config[4][1] = other
        state.config[4][2] = other

        state.config[4][6] = other
        state.config[4][7] = other
        state.config[4][8] = other

        moves = list(state.possible_move_from(4, 4))
        correct_moves = [(6, 4), (4, 1)]
        return set(moves) == set(correct_moves)

    def test_possible_move_from_direction(self):
        state = GameState()
        move = state.possible_move_from_direction(4, 4, -1, 1)
        assert move is None

    def test_possible_moves_of_state(self):
        state = GameState()
        moves = list(state.possible_moves())
        correct_moves = [(5, 3), (6, 4), (4, 6), (3, 5)]
        assert set(moves) == set(correct_moves)

    def test_next_state_by_moving_to(self):
        state = GameState()
        state = state.next_state_by_moving_to(6, 4)

        correct_state = GameState()

        correct_state.config[6][4] = correct_state.current_player
        correct_state.config[5][4] = correct_state.current_player
        correct_state.flip_player()

        assert state == correct_state

    def test_next_after_initial_states(self):
        state = GameState()
        ans = state.next_states()
        first = GameState(current_player=JMIN)
        first.config[3][5] = JMAX
        first.config[4][5] = JMAX

        second = GameState(current_player=JMIN)
        second.config[4][5] = JMAX
        second.config[4][6] = JMAX

        third = GameState(current_player=JMIN)
        third.config[6][4] = JMAX
        third.config[5][4] = JMAX

        fourth = GameState(current_player=JMIN)
        fourth.config[5][3] = JMAX
        fourth.config[5][4] = JMAX

        assert set(ans) == {first, second, third, fourth}
