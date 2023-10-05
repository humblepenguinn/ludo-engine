class Piece:
    def __init__(self):
        self.position = -1
        self.locked = True

    def move(self, steps):
        if not self.locked:
            self.position += steps
            if self.position > 57:
                self.position = 57
            return self.position
