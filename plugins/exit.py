from core.plugin_base import PluginBase


class ExitPlugin(PluginBase):

    def register(self, game):

        def exit_game():
            confirm = input("Are you sure? [Y/N]: ").upper()
            if confirm == "Y":
                game.running = False

        game.register_command("EXIT", exit_game)
