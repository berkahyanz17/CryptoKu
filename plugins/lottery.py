import random
from core.plugin_base import PluginBase

class LotteryPlugin(PluginBase):
    def register(self, game):
        def lottery_command():
            bet = 10000

            if game.player.money < bet:
                print("Not enough money.")
                return

            game.player.remove_money(bet)

            if random.randint(1, 100) <= 10:
                reward = 200000
                game.player.add_money(reward)
                print(f"You won {reward}!")
            else:
                print("You lost.")

        game.register_command("LOTTERY", lottery_command)