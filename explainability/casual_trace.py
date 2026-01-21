class CasualTrace:
    def __init__(self):
        self.links = []

    def add(self, cause, effect):
        self.links.append((cause, effect))