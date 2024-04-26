from source.players import Player


class Narrator:
    def __init__(self, first_player: Player, second_player: Player):
        self.first_player = first_player
        self.second_player = second_player

    def narrate_action(self, action: dict, active_player: Player) -> str:

        enemy = self.second_player if active_player is self.first_player else self.first_player

        if action["kind"] in ("hit", "special"):
            return f"{active_player.get_name()} golpea con un {action['name'].lower()} a {enemy.get_name()}"


        if action["kind"] == "movement":
            moves = {
                "W": "arriba",
                "S": "la izquierda",
                "A": "abajo",
                "D": "la derecha",
            }

            narration = f"{active_player.get_name()} se mueve hacia "
            for index, move in enumerate(action["name"], start=1):
                movement = moves.get(move)
                narration += f"{movement} y " if (len(action["name"]) - 1) == index else f"{movement},"


            return narration.rstrip(",")

    def summarize(self) -> str:
        summary = "Resumen del combate:\n"
        summary += f"{self.first_player.get_name()} - Salud: {self.first_player.get_health()} puntos\n"
        summary += f"{self.second_player.get_name()} - Salud: {self.second_player.get_health()} puntos\n"
        return summary
