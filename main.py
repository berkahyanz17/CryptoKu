from core.game import Game
from core.plugin_loader import PluginLoader


def main():
    print("//// WELCOME TO JOEDIAPP ENGINE ////")
    name = input("Enter your name: ").strip()

    # Initialize game
    game = Game(name)

    # Load plugins dynamically
    loader = PluginLoader(plugin_folder="plugins")
    loader.load_plugins(game)

    print("\nType commands. Type EXIT to quit.\n")

    # Main loop
    while game.running:
        try:
            command = input(">> ").strip()

            if not command:
                continue

            game.router.dispatch(command)
            game.save_game()

        except KeyboardInterrupt:
            print("\nExiting game...")
            break

        except Exception as e:
            print(f"Runtime error: {e}")

    print("Game closed.")


if __name__ == "__main__":
    main()

# from core.plugin_loader import PluginLoader

# def main():
#     game = Game("Player")

#     loader = PluginLoader()
#     loader.load_plugins(game)

#     while True:
#         cmd = input(">> ")
#         game.router.dispatch(cmd)

# from core.game import Game
# from core.router import CommandRouter

# def main():
#     name = input("Enter name: ")
#     game = Game(name)
#     router = CommandRouter(game)

#     while game.running:
#         cmd = input(">> ")
#         router.dispatch(cmd)

# if __name__ == "__main__":
#     main()