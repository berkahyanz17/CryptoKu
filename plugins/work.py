import random
from core.plugin_base import PluginBase


class WorkPlugin(PluginBase):
    name = "Work System"

    def register(self, game):

        def work():
            if game.player.stamina < 50:
                print("Not enough stamina.")
                return

            game.player.stamina -= 50

            roll = random.randint(1, 100)

            if roll <= 30:
                print("No bonus today.")
            elif roll <= 80:
                salary = random.randint(10000, 50000)
                game.player.money += salary
                print(f"You earned {salary}.")
            else:
                salary = random.randint(150000, 300000)
                game.player.money += salary
                print(f"Big bonus! Earned {salary}.")

        game.register_command("WORK", work)
