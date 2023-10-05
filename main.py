from engine import Game

from engine.move import MoveForward, UnlockPiece

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


if __name__ == "__main__":
  num_players = 1
  ais = [ai1] # the engine will run the ai for the player, with respect to its position in the list. So the first element (ai) will be run for the first player. 

  game = Game(num_players, ais)
  game.main()

