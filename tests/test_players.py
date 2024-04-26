from source import players



def test_check_attack_system(commands):
    tony_commands, arnold_commands = commands["player1"], commands["player2"]

    arnold = players.ArnaldorShuatseneguer(commands=arnold_commands)
    tony = players.TonynStallone(commands=tony_commands)

    tony_attack_action = tony.attack(enemy=arnold)

    assert tony_attack_action["kind"] == "hit"
    assert arnold.get_health() == 5
    assert tony.get_health() == 6

    arnold_attack_action = arnold.attack(enemy=tony)
    assert arnold_attack_action["kind"] == "special"
    assert arnold.get_health() == 5
    assert tony.get_health() == 3


def test_remaining_command_logic_is_consistent_after_each_attack(commands):
    tony_commands, arnold_commands = commands["player1"], commands["player2"]

    tony = players.TonynStallone(commands=tony_commands)
    arnold = players.ArnaldorShuatseneguer(commands=arnold_commands)

    assert tony.no_commands_remaining() is False

    for _ in range(len(tony_commands["movimientos"])):
        assert tony.no_commands_remaining() is False
        tony.attack(enemy=arnold)

    assert tony.no_commands_remaining()