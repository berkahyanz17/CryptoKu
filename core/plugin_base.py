from abc import ABC, abstractmethod

class PluginBase(ABC):
    name = "Unnamed Plugin"
    version = "1.0"

    @abstractmethod
    def register(self, game):
        """
        Called when plugin is loaded.
        Must register commands via game.register_command()
        """
        pass
