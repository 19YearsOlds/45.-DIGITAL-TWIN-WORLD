class PopulationSystem:
    def __init__(self, population):
        self.population = population

    def step(self, food_index):
        self.population *= (1.01 if food_index > 0.8 else 0.99)