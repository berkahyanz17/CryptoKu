from core.plugin_base import PluginBase


class StatPlugin(PluginBase):
    name = "Player Stats"

    def register(self, game):

        def stat():
            print("=== PLAYER STAT ===")
            print(f"Name: {game.player.name}")
            print(f"Money: {game.player.money}")
            print(f"Stamina: {game.player.stamina}")

        game.register_command("STAT", stat)
