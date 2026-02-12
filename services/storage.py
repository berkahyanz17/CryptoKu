import json
from models.player import Player
from core.config import CONFIG


class Storage:
    def __init__(self, filename=CONFIG.SAVE_FILE):
        self.filename = filename

    def save(self, player):
        data = {
            "name": player.name,
            "money": player.money,
            "stamina": player.stamina,
            "crypto_wallet": player.crypto_wallet,
            "inventory": player.inventory,
        }

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)

            return Player(
                name=data["name"],
                money=data["money"],
                stamina=data["stamina"],
                crypto_wallet=data.get("crypto_wallet", {}),
                forex_positions={},
                inventory=data.get("inventory", {})
            )

        except FileNotFoundError:
            return None

    def create_new_player(self, name):
        return Player(
            name=name,
            money=CONFIG.STARTING_MONEY,
            stamina=CONFIG.STARTING_STAMINA
        )
