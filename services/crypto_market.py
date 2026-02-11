import random


class CryptoMarket:
    def __init__(self):
        self.prices = {
            "Cryptid": 1000.0,
            "Viscoin": 500.0,
            "Monggot": 2500.0,
        }

    def update_market(self):
        for coin in self.prices:
            change = random.uniform(-0.1, 0.1)
            self.prices[coin] = round(self.prices[coin] * (1 + change), 2)

    def buy(self, player, coin, amount_money):
        price = self.prices[coin]
        if not player.remove_money(amount_money):
            return False, "Not enough money"

        qty = amount_money / price
        player.add_crypto(coin, qty)

        return True, qty

    def sell(self, player, coin, qty):
        if not player.remove_crypto(coin, qty):
            return False, "Not enough holdings"

        value = qty * self.prices[coin]
        player.add_money(value)

        return True, value
