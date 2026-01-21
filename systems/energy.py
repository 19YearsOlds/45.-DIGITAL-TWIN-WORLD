class EnergySystem:
    def __init__(self, fossil_share):
        self.fossil_share = fossil_share

    def emissions(self):
        return self.fossil_share * 10