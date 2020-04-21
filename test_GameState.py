from unittest import TestCase
from unittest import skip
from GameState import *
from helper import *


class TestGameState(TestCase):

    def setUp(self) -> None:
        self.state = GameState()

    @skip("Not implemented")
    def test_is_final(self):
        self.fail()

    @skip("Not implemented")
    def test_winner(self):
        self.fail()

    def test_next_player(self):
        state = GameState(current_player=JMAX)
        assert state.next_player() == JMIN

        state = GameState(current_player=JMIN)
        assert state.next_player() == JMAX

    @skip("Not implemented")
    def test_score(self):
        self.fail()

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

    @skip("Not implemented")
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

        assert ans == [first, second, third, fourth]
