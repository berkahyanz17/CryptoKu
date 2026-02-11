class Player:
    def __init__(self, name, money, stamina, crypto_wallet=None, forex_positions=None):
        self.name = name
        self.money = money
        self.stamina = stamina
        self.crypto_wallet = crypto_wallet or {}
        self.forex_positions = forex_positions or {}

    # ---- Money ----
    def add_money(self, amount):
        self.money += amount

    def remove_money(self, amount):
        if amount > self.money:
            return False
        self.money -= amount
        return True

    # ---- Crypto ----
    def add_crypto(self, coin, amount):
        self.crypto_wallet[coin] = self.crypto_wallet.get(coin, 0) + amount

    def remove_crypto(self, coin, amount):
        if self.crypto_wallet.get(coin, 0) < amount:
            return False
        self.crypto_wallet[coin] -= amount
        return True

    # ---- Forex ----
    def add_position(self, position):
        self.forex_positions[position.id] = position

    def remove_position(self, pos_id):
        if pos_id in self.forex_positions:
            del self.forex_positions[pos_id]
