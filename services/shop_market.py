import random
import random


class ShopMarket:
    def __init__(self):
        self.items = {
            "Water": {
                "base_price": 5000,
                "effect": {"stamina": 20}
            },
            "Coffee": {
                "base_price": 10000,
                "effect": {"stamina": 35}
            },
            "EnergyDrink": {
                "base_price": 20000,
                "effect": {"stamina": 50}
            },
            "Bread": {
                "base_price": 8000,
                "effect": {}
            },
            "SuperPotion": {
                "base_price": 50000,
                "effect": {"stamina": 100}
            }
        }

        self.current_prices = {
            name: data["base_price"]
            for name, data in self.items.items()
        }

    def consume(self, player, item):
        if item not in self.items:
            return False, "Item does not exist"

        if not player.remove_item(item, 1):
            return False, "You don't have this item"

        effect = self.items[item]["effect"]

        if "stamina" in effect:
            player.add_stamina(effect["stamina"])


        return True, f"Consumed {item}"

