class EconomySystem:
    def __init__(self, gdp):
        self.gdp = gdp

    def grow(self, climate_damage):
        self.gdp *= (1.02 - climate_damage)