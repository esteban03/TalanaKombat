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


@pytest.fixture()
def just_movement_command():
    data = {
        "player1": {
            "movimientos": [
                "DSD",
            ],
            "golpes": [
                "",
            ]
        },
        "player2": {
            "movimientos": [
                "SA",
            ],
            "golpes": [
                "",
            ]
        }
    }

    return data


@pytest.fixture()
def just_special_command():
    data = {
        "player1": {
            "movimientos": [
                "DSD",
            ],
            "golpes": [
                "P",
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

    return data