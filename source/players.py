from contextlib import suppress

class Player:
    _life = 6
    _name: str
    _specials: dict
    _controls = {
        "P": (1, "Puñetazo"),
        "K": (1, "Patada"),
        "W": (0, "Arriba"),
        "S": (0, "Izquierda"),
        "A": (0, "Abajo"),
        "D": (0, "Derecha"),
    }
    _commands: dict

    def __init__(self, commands: dict) -> None:
        self._commands = commands

    def get_name(self) -> str:
        return self._name

    def alive(self) -> bool:
        return self._life > 0

    def get_commands(self) -> dict:
        return self._commands.copy()

    def _make_damage(self, amount: int) -> None:
        if (self._life - amount) < 0:
            self._life = 0

        self._life -= amount

    def _get_effects_to_attack(self,) -> tuple[int, str, str]:
        movements, hit = self.next_command()

        if (special := self._specials.get(movements + hit)) is not None:
            damage, action = special
            return damage, action, "special"

        if movements != "" and hit != "":
            damage, action = self._controls[hit]
            return damage, action, "hit"

        if movements != "" and hit == "":
            return 0, movements, "movement"

        if movements == "" and hit != "":
            damage, action = self._controls[hit]
            return damage, action, "hit"

    def attack(self, enemy: 'Player') -> dict:
        damage, action, kind = self._get_effects_to_attack()

        enemy._make_damage(amount=damage)

        return dict(kind=kind, name=action)

    def next_command(self) -> tuple[str, str]:
        movements = ""
        with suppress(IndexError):
            movements = self._commands["movimientos"].pop(0)

        hit = ""
        with suppress(IndexError):
            hit = self._commands["golpes"].pop(0)

        return movements, hit


class TonynStallone(Player):
    _name = "Tonyn Stallone"
    _specials = {
        "DSDP": (3, "Taladoken"),
        "SDK": (2, "Remuyuken"),
    }


class ArnaldorShuatseneguer(Player):
    _name = "Arnaldor Shuatseneguer"
    _specials = {
        "SAK": (3, "Remuyuken"),
        "ASAP": (2, "Taladoken"),
    }

