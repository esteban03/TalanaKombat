import pytest

from source.main import Kombat
from source import players

first_player_with_less_total_commands = {
    "player1": {
        "movimientos": [
            "D",
        ],
        "golpes": [
            "K",
        ]
    },
    "player2": {
        "movimientos": [
            "SA","SA",
        ],
        "golpes": [
            "K", "K",
        ]
    }
}

second_player_with_less_total_commands = {
    "player1": {
        "movimientos": [
            "D", "DSD",
        ],
        "golpes": [
            "K", "P",
        ]
    },
    "player2": {
        "movimientos": [
            "SA",
        ],
        "golpes": [
            "K",
        ]
    }
}

first_player_with_less_total_movements = {
    "player1": {
        "movimientos": [
            "D",
        ],
        "golpes": [
            "K", "P", "P",
        ]
    },
    "player2": {
        "movimientos": [
            "SA", "SA",
        ],
        "golpes": [
            "K", "K",
        ]
    }
}

symmetrical_commands = {
    "player1": {
        "movimientos": [
            "SA", "SA",
        ],
        "golpes": [
            "K", "K",
        ]
    },
    "player2": {
        "movimientos": [
            "SA", "SA",
        ],
        "golpes": [
            "K", "K",
        ]
    }
}


@pytest.mark.parametrize("commands, active_expected, enemy_expected", [
    (first_player_with_less_total_commands, players.TonynStallone, players.ArnaldorShuatseneguer),
    (second_player_with_less_total_commands, players.ArnaldorShuatseneguer, players.TonynStallone),
    (first_player_with_less_total_movements, players.TonynStallone, players.ArnaldorShuatseneguer),
    (symmetrical_commands, players.TonynStallone, players.ArnaldorShuatseneguer),
])
def test_choose_starting_player_logic_and_second_player_start(commands, active_expected, enemy_expected):
    tony_commands, arnold_commands = commands["player1"], commands["player2"]

    tony = players.TonynStallone(commands=tony_commands)
    arnold = players.ArnaldorShuatseneguer(commands=arnold_commands)

    game = Kombat(first_player=tony, second_player=arnold)

    game._choose_starting_player()

    assert isinstance(game.get_active_player(), active_expected)
    assert isinstance(game.get_enemy_player(), enemy_expected)