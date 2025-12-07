import random


class Skin:
    def __init__(self, name, rarity, base_price):
        self.name = name
        self.rarity = rarity
        self.float_value = round(random.uniform(0.00, 1.00), 4)
        self.base_price = base_price

    def get_price(self):

        wear_multiplier = 1 - self.float_value
        return round(self.base_price * (1 + wear_multiplier), 2)

    def describe(self):
        return (
            f"Скін: {self.name} | Рідкість: {self.rarity} | "
            f"Float: {self.float_value} | Ціна: ${self.get_price()}"
        )


class Case:
    def __init__(self, name, skins):
        self.name = name
        self.skins = skins

        self.drop_rates = {
            "Consumer": 0.7992,
            "Industrial": 0.1598,
            "Mil-Spec": 0.0799,
            "Restricted": 0.0159,
            "Classified": 0.00319,
            "Covert": 0.00064,
            "Knife": 0.00027
        }

    def open(self):
        rarities = list(self.drop_rates.keys())
        weights = list(self.drop_rates.values())

        chosen_rarity = random.choices(rarities, weights=weights, k=1)[0]

        available_skins = [s for s in self.skins if s.rarity == chosen_rarity]

        if not available_skins:
            return random.choice(self.skins)

        return random.choice(available_skins)


skins = [
    Skin("Urban Camo", "Consumer", 0.5),
    Skin("Sand Storm", "Industrial", 1.2),
    Skin("Night Ops", "Mil-Spec", 4.0),
    Skin("Crimson Web", "Restricted", 12.0),
    Skin("Hyper Beast", "Classified", 45.0),
    Skin("Dragon Lore", "Covert", 150.0),
    Skin("Karambit Fade", "Knife", 800.0)
]


cs_case = Case("CS2 Weapon Case", skins)


dropped_skin = cs_case.open()
print(dropped_skin.describe())
