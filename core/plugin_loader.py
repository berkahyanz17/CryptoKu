import os
import importlib
from core.plugin_base import PluginBase

class PluginLoader:
    def __init__(self, plugin_folder="plugins"):
        self.plugin_folder = plugin_folder

    def load_plugins(self, game):
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith(".py") and not filename.startswith("_"):
                module_name = filename[:-3]

                module = importlib.import_module(
                    f"{self.plugin_folder}.{module_name}"
                )

                for attribute in dir(module):
                    obj = getattr(module, attribute)

                    if isinstance(obj, type) and issubclass(obj, PluginBase) and obj != PluginBase:
                        plugin_instance = obj()
                        plugin_instance.register(game)
                        print(f"Loaded plugin: {module_name}")
