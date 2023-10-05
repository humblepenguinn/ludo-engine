from .piece import Piece

class Player:
    def __init__(self, name, ai=None):
        self.name = name
        self.pieces = [Piece() for i in range(4)]
        self.ai = ai

