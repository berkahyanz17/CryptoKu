class Position:
    def __init__(self, pos_id, pair, direction, entry_price, volume, margin):
        self.id = pos_id
        self.pair = pair
        self.direction = direction  # "BUY" or "SELL"
        self.entry_price = entry_price
        self.volume = volume
        self.margin = margin

    def calculate_pnl(self, current_price):
        multiplier = 1 if self.direction == "BUY" else -1
        return (current_price - self.entry_price) * 100000 * self.volume * multiplier
