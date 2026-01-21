class Coupler:
    def step(self, climate, economy, population, energy, food):
        emissions = energy.emissions()
        climate.step(emissions)
        food.step(climate.temperature)
        economy.grow(climate_damage=0.001 * climate.temperature)
        population.step(food.yield_index)