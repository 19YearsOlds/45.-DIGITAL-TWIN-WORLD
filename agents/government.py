class Government:
    def __init__(self, tax):
        self.tax = tax

    def policy_emissions_tax(self):
        return self.tax * 0.5