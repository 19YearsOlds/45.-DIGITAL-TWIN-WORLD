class SimulationClock:
    def __init__(self):
        self.year = 0

    def tick(self):
        self.year += 1