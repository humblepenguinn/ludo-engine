from .piece import Piece
from .player import Player


class Move:
    def __init__(self, piece: Piece, dice: int):
        self.piece = piece
        self.dice = dice

    def validate(self) -> (bool, str):
        raise NotImplementedError


class MoveForward(Move):
    def validate(self) -> (bool, str):
        if (self.piece.position + self.dice <= 57) and (not self.piece.locked):
            return (True, "")

        if self.piece.locked:
            return (False, "Piece is locked")

        return (False, "Piece cannot move that far forward (would exceed 57)")

    def __repr__(self):
        return f"MoveForward({self.piece}, {self.dice})"


class UnlockPiece(Move):
    def validate(self) -> (bool, str):
        if self.dice == 6 and self.piece.locked:
            return (True, "")

        if self.dice != 6:
            return (False, "Dice is not 6")

        return (False, "Piece is already unlocked")

    def __repr__(self):
        return f"UnlockPiece({self.piece})"


class KillPiece(Move):
    def __repr__(self):
        return f"KillPiece({self.piece})"


def handle_move(move: Move, player: Player, safe_spots):
    if isinstance(move, MoveForward):
        new_position = move.piece.move(move.dice)

        if new_position in safe_spots:
            print(
                f"{player.name} landed on a safe spot {new_position}. Stay here.\n"
            )

        elif new_position == 57:
            print(f"{player.name} piece [{move.piece}] won!\n")
            return

        else:
            print(f"{player.name} moved to position {new_position}\n")


    elif isinstance(move, UnlockPiece):
        move.piece.locked = False
        move.piece.position = 0

        piece_num = player.pieces.index(move.piece) + 1

        print(
            f"{player.name}'s piece [{piece_num}] unlocked! New position: 0.\n")

    elif isinstance(move, KillPiece):
        print("KillPiece not implemented yet\n")

    else:
        print(f"Invalid move: {move}")
        return
