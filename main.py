from source.main import Kombat
from source.players import TonynStallone, ArnaldorShuatseneguer

# necesitamos un datamanager
data = {
    "player1": {
        "movimientos": ["D", "DSD", "S", "DSD", "SD"],
        "golpes": ["K", "P", "", "K", "P"]
    },
    "player2": {
        "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
        "golpes": ["K", "", "K", "P", "P"]
    }
}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    first_player = TonynStallone(commands=data["player1"])
    second_player = ArnaldorShuatseneguer(commands=data["player2"])

    game = Kombat(
       first_player=first_player,
       second_player=second_player,
    )

    game.start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
