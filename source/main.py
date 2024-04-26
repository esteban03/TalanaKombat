from contextlib import suppress

from source.narrator import Narrator
from source.players import Player


class Kombat:
    _active_player: Player
    _enemy_player: Player

    def __init__(self, first_player: Player, second_player: Player):
        self.first_player = first_player
        self.second_player = second_player

    def _choose_starting_player(self) -> None:
        self._active_player = self.first_player
        self._enemy_player = self.second_player

        first_player_commands = self.first_player.get_commands()
        second_player_commands = self.second_player.get_commands()

        first_player_total_movements = len(first_player_commands["movimientos"])
        second_player_total_movements = len(second_player_commands["movimientos"])

        first_player_total_hits = len(first_player_commands["golpes"])
        second_player_total_hits = len(second_player_commands["golpes"])

        first_player_total_commands = first_player_total_movements + first_player_total_hits
        second_player_total_commands = second_player_total_movements + second_player_total_hits

        # Check the total commands to start
        if first_player_total_commands < second_player_total_commands:
            self._active_player = self.first_player
            self._enemy_player = self.second_player
            return

        if second_player_total_commands < first_player_total_commands:
            self._active_player = self.second_player
            self._enemy_player = self.first_player
            return


        # Check the total movements
        if first_player_total_movements < second_player_total_movements:
            self._active_player = self.first_player
            self._enemy_player = self.second_player
            return

        if second_player_total_movements < first_player_total_movements:
            self._active_player = self.second_player
            self._enemy_player = self.first_player
            return


        # check the total hits
        if first_player_total_hits < second_player_total_hits:
            self._active_player = self.first_player
            self._enemy_player = self.second_player
            return

        if second_player_total_hits < first_player_total_hits:
            self._active_player = self.second_player
            self._enemy_player = self.first_player
            return


    def start(self) -> None:
        print("*" * 30)
        print("Inicia el juego")
        print("*" * 30)
        print("")

        self._choose_starting_player()
        narrator = Narrator(first_player=self.first_player, second_player=self.second_player)

        while not self._gameover():
            player = self._get_active_player()

            if player.no_commands_remaining():
                break

            action = player.attack(enemy=self._get_enemy_player())

            narration = narrator.narrate_action(action=action, active_player=self._active_player)
            print(narration)

            self._next_turn()

        print("")
        print("*" * 30)
        print(narrator.summarize())

        print("*" * 30)
        print("Finaliza el juego")
        print("*" * 30)

    def _gameover(self) -> bool:
        return not self.first_player.alive() or not self.second_player.alive()

    def _get_active_player(self) -> Player:
        return self._active_player

    def _get_enemy_player(self) -> Player:
        return self._enemy_player

    def _next_turn(self) -> None:
        self._active_player, self._enemy_player = self._enemy_player, self._active_player


