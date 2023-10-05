from random import randint

from .player import Player
from .move import Move, handle_move

class Game:
    def __init__(self, num_players, ais):
        self.num_players = num_players
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.safe_spots = {0, 8, 13, 21, 26, 34, 39, 47, 52, 53, 54, 55, 56}
        self.board = [" " for i in range(57)]

        for index, ai in enumerate(ais):
            self.players[index].ai = ai

    def roll_dice(self):
        return (randint(1, 6), randint(1, 6))

    def is_game_over(self):
        for player in self.players:
            if all(piece.position == 57 for piece in player.pieces):
                print(f"Congratulations, {player.name}! You won!")
                return True

            # if player.pieces[0].locked == False and player.pieces[1].locked == False:
            #     print(f"Congratulations, {player.name}! You won!")
            #     return True
        return False

    def play_turn(self, player):
        print(f"[{player.name}]")

        dice = self.roll_dice()
        print(f"{player.name} rolled {dice}\n")

        try:
            moves = player.ai(dice, player.pieces,
                                  self.board, self.safe_spots)
        except Exception as e:
            print(
                f"Error while running {player.name}'s AI. Skipping turn. Here are the details of the exception: {e}\n"
            )
            return

        if moves == None:
            return # Skip turn

        if len(moves) > 2:
            print(f"Invalid number of moves: {moves}\n")
            return

        for move in moves:
            is_valid, reason = move.validate()

            if not isinstance(move, Move) or not is_valid:
                print(f"Invalid move: {move} ({reason})\n")
                return

            handle_move(move, player, dice, self.safe_spots)

        self.update_board(player)

    def update_board(self, player):
        for piece in player.pieces:
            if piece.position == -1:
                continue

            if self.board[piece.position - 1] != " ":
                self.board[piece.position -
                           1] = self.board[piece.position - 1] + " " + player.name
                continue

            self.board[piece.position - 1] = player.name

    def main(self):
        while True:
            for player in self.players:
                if self.is_game_over():
                    return

                self.play_turn(player)
                from . import piece
