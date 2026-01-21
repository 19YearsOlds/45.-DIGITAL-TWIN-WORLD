from systems. climate import ClimateSystem
from systems.economy import EconomySystem
from system.population import PopulationSystem
from systems.energy import EnergySystem
from systems.food import FoodSystem
from coupling.system_coupler import Coupler
from prediction.forward_simulator import run

climate = ClimateSystem(14, 415)
economy = EconomySystem(100)
population = PopulationSystem(8)
energy = EnergySystem(0.8)
food = FoodSystem(1.0)

systems = [climate, economy, population, energy, food]
coupler = Coupler()

history = run(None, systems, coupler, 30)

for year, state in enumerate(history):
    print(year, state)