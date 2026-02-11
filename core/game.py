from services.crypto_market import CryptoMarket
from services.forex_market import ForexMarket
from services.storage import Storage
from core.router import CommandRouter

class Game:
    def __init__(self, player_name):
        self.router = CommandRouter()
        self.storage = Storage()

        saved_player = self.storage.load()

        if saved_player:
            print("Loaded saved game.")
            self.player = saved_player
        else:
            print("Creating new player.")
            self.player = self.storage.create_new_player(player_name)

        self.crypto_market = CryptoMarket()
        self.forex_market = ForexMarket()

        self.running = True

    def register_command(self, name, handler):
        self.router.register(name, handler)

    def save_game(self):
        self.storage.save(self.player)

