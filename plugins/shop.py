from core.plugin_base import PluginBase


class ShopPlugin(PluginBase):

    def register(self, game):

        def shop():

            # game.shop_market.update_prices()

            print("\n=== MARKET ===")
            for item, price in game.shop_market.current_prices.items():
                owned = game.player.inventory.get(item, 0)
                print(f"{item} | Price: {price} | You have: {owned}")

            print("\n[B]uy  [S]ell  [C]onsume  [X]Exit")
            action = input(">> ").upper()

            if action == "B":
                item = input("Item name: ")
                qty = int(input("Quantity: "))

                success, result = game.shop_market.buy(
                    game.player,
                    item,
                    qty
                )

                if success:
                    print(f"Purchased for {result}")
                else:
                    print(result)

            elif action == "S":
                item = input("Item name: ")
                qty = int(input("Quantity: "))

                success, result = game.shop_market.sell(
                    game.player,
                    item,
                    qty
                )

                if success:
                    print(f"Sold for {result}")
                else:
                    print(result)
            
            elif action == "C":
                item = input("Item name: ")

                success, result = game.shop_market.consume(
                    game.player,
                    item
                )

                print(result)
            elif action == "X":
                return

        game.register_command("SHOP", shop)
