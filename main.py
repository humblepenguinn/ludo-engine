from engine import Game

from engine.move import MoveForward, UnlockPiece

piece_one = 0
piece_two = 0

'''
A very very very simple AI.
'''
def ai1(dice, pieces, board, safe_spots):
  if dice == (6, 6):
    return [UnlockPiece(pieces[0], dice[0]), UnlockPiece(pieces[1], dice[1])]

  if dice[0] == 6:
    return [UnlockPiece(pieces[0], dice[0])]

  if dice[1] == 6:
    return [UnlockPiece(pieces[1], dice[1])]

  return None



# def ai2(dice, pieces, board, safe_spots):
#   global piece_two

#   piece_two += 1

#   if piece_two == 5:
#     piece_two = 1

#   return piece_two


if __name__ == "__main__":
  num_players = 1
  ais = [ai1]

  game = Game(num_players, ais)
  game.main()

