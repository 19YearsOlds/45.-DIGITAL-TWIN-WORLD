class FoodSystem:
    def __init(self, yield_index):
        self.yield_index = yield_index

    def step(self, temperature):
        self.yield_index -= 0.01 * abs(temperature - 14)