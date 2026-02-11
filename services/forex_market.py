import random
from models.position import Position


class ForexMarket:
    def __init__(self):
        self.prices = {
            "EUR/USD": 1.10,
            "USD/JPY": 150.0
        }
        self.next_id = 1

    def update_market(self):
        for pair in self.prices:
            change = random.uniform(-0.01, 0.01)
            self.prices[pair] = round(self.prices[pair] * (1 + change), 4)

    def open_position(self, player, pair, direction, volume):
        price = self.prices[pair]
        margin = volume * 100000

        if not player.remove_money(margin):
            return False, "Insufficient funds"

        position = Position(
            self.next_id,
            pair,
            direction,
            price,
            volume,
            margin
        )

        player.add_position(position)
        self.next_id += 1

        return True, position

    def close_position(self, player, pos_id):
        if pos_id not in player.forex_positions:
            return False, "Invalid position ID"

        position = player.forex_positions[pos_id]
        current_price = self.prices[position.pair]
        pnl = position.calculate_pnl(current_price)

        player.add_money(position.margin + pnl)
        player.remove_position(pos_id)

        return True, pnl
