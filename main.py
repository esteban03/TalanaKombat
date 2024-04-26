import json

from source.main import Kombat
from source.players import TonynStallone, ArnaldorShuatseneguer

def reader(file: str, path="./data/") -> dict:
    with open(path + file) as file:
        data = json.load(file)

    return data


if __name__ == '__main__':

    data = reader(file="commands.json")

    first_player = TonynStallone(commands=data["player1"])
    second_player = ArnaldorShuatseneguer(commands=data["player2"])

    game = Kombat(
       first_player=first_player,
       second_player=second_player,
    )

    game.start()
