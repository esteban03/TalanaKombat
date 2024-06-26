import pytest

from source.main import Kombat
from source import players

def test_kombat_winner(commands):
    tony_commands, arnold_commands = commands["player1"], commands["player2"]

    tony = players.TonynStallone(commands=tony_commands)
    arnold = players.ArnaldorShuatseneguer(commands=arnold_commands)

    game = Kombat(first_player=tony, second_player=arnold)
    game.start()

    assert not tony.alive()
    assert arnold.alive()


def test_turn_change_logic(commands):
    tony_commands, arnold_commands = commands["player1"], commands["player2"]

    tony = players.TonynStallone(commands=tony_commands)
    arnold = players.ArnaldorShuatseneguer(commands=arnold_commands)

    game = Kombat(first_player=tony, second_player=arnold)
    game._active_player = tony
    game._enemy_player = arnold

    assert game._get_active_player() is tony
    assert game._get_enemy_player() is arnold

    game._next_turn()

    assert game._get_active_player() is arnold
    assert game._get_enemy_player() is tony


@pytest.mark.parametrize("tony_life, arnold_life, result_expected", [
    (6, 6, False),
    (6, 0, True),
    (0, 6, True),
    (0, 0, True),
])
def test_gameover_logic(commands, tony_life, arnold_life, result_expected):
    tony_commands, arnold_commands = commands["player1"], commands["player2"]

    tony = players.TonynStallone(commands=tony_commands)
    tony._life = tony_life

    arnold = players.ArnaldorShuatseneguer(commands=arnold_commands)
    arnold._life = arnold_life

    game = Kombat(first_player=tony, second_player=arnold)

    assert game._gameover() == result_expected



