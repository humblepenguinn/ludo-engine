class Strategy:
    def __init__(self, name):
        self.name = name

    def run(self):
        raise NotImplementedError(
            "Strategy.run() is not implemented. You must implement this method")

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name
