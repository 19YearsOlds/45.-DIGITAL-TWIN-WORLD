class ClimateSystem:
    def __init__(self, temp, co2):
        self.temperature = temp
        self.co2 = co2

    def step(self, emissions):
        self.co2 += emissions
        self.temperature += 0.01 * emissions