class CONFIG:
    SAVE_FILE = "save.json"
    STARTING_MONEY = 100_000
    STARTING_STAMINA = 100

    WIN_CONDITION = 1_000_000_000

    FOREX = {
        "MARGIN_PER_LOT": 10_000_000,
        "PIP_VALUE": 100_000,
    }

    CRYPTO = {
        "Cryptid": {"stability": 0.15, "weight": 5},
        "Viscoin": {"stability": 0.30, "weight": 10},
        "Monggot": {"stability": 0.10, "weight": 2},
    }
