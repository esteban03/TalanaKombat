import pytest


@pytest.fixture
def commands():
    data = {
        "player1": {
            "movimientos": [
                "D",
                "DSD",
                "S",
                "DSD",
                "SD"
            ],
            "golpes": [
                "K",
                "P",
                "",
                "K",
                "P"
            ]
        },
        "player2": {
            "movimientos": [
                "SA",
                "SA",
                "SA",
                "ASA",
                "SA"
            ],
            "golpes": [
                "K",
                "",
                "K",
                "P",
                "P"
            ]
        }
    }

    return data


