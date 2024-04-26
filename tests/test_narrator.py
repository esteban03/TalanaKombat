from source.narrator import Narrator
from source import players


def test_hit_narration(commands):
    tony_commands, arnold_commands = commands["player1"], commands["player2"]

    tony = players.TonynStallone(commands=tony_commands)
    arnold = players.ArnaldorShuatseneguer(commands=arnold_commands)

    tony_attack_action = tony.attack(enemy=arnold)

    narrator = Narrator(first_player=tony, second_player=arnold)

    narration = narrator.narrate_action(active_player=tony, action=tony_attack_action)

    assert narration == "Tonyn Stallone golpea con un patada a Arnaldor Shuatseneguer"

def test_movement_narration(just_movement_command):
    tony_commands, arnold_commands = just_movement_command["player1"], just_movement_command["player2"]

    tony = players.TonynStallone(commands=tony_commands)
    arnold = players.ArnaldorShuatseneguer(commands=arnold_commands)

    tony_attack_action = tony.attack(enemy=arnold)

    narrator = Narrator(first_player=tony, second_player=arnold)

    narration = narrator.narrate_action(active_player=tony, action=tony_attack_action)

    assert narration == "Tonyn Stallone se mueve hacia la derecha,la izquierda y la derecha"


def test_special_hit_narration(just_special_command):
    tony_commands, arnold_commands = just_special_command["player1"], just_special_command["player2"]

    tony = players.TonynStallone(commands=tony_commands)
    arnold = players.ArnaldorShuatseneguer(commands=arnold_commands)

    tony_attack_action = tony.attack(enemy=arnold)

    narrator = Narrator(first_player=tony, second_player=arnold)

    narration = narrator.narrate_action(active_player=tony, action=tony_attack_action)

    assert narration == "Tonyn Stallone golpea con un taladoken a Arnaldor Shuatseneguer"