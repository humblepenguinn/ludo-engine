from engine import Game

from engine.move import MoveForward, UnlockPiece

'''
A very very very very simple AI.

This is perhaps the most shittest AI that a person can write.

Please do not make an AI like this. It is very bad. I am not joking.

If you want to expand this to 4 players, you can do so by adding more locked_pieces and unlocked_pieces lists for each player and then creating a new ai function for each player that uses the correct lists.
'''

locked_pieces = [0, 1, 2, 3]
unlocked_pieces = []

def ai(dice, pieces, board, safe_spots):
    global locked_pieces
    global unlocked_pieces


    if dice == (6, 6) and len(locked_pieces) > 0:
        piece_to_move = locked_pieces.pop()
        unlocked_pieces.append(piece_to_move)
        return [UnlockPiece(pieces[piece_to_move], dice[0]), UnlockPiece(pieces[piece_to_move], dice[1])]

    if dice[0] == 6 and len(locked_pieces) > 0:
        piece_to_move = locked_pieces.pop()
        unlocked_pieces.append(piece_to_move)
        return [UnlockPiece(pieces[piece_to_move], dice[0])]

    if dice[1] == 6 and len(locked_pieces) > 0:
        piece_to_move = locked_pieces.pop()
        unlocked_pieces.append(piece_to_move)
        return [UnlockPiece(pieces[piece_to_move], dice[1])]

    moves = []
    dice_index = 0

    for idx, piece_index in enumerate(unlocked_pieces):
        if pieces[piece_index].position >= 57:
            del unlocked_pieces[idx]
            continue

        if pieces[piece_index].position + dice[dice_index] <= 57:
            moves.append(MoveForward(pieces[piece_index], dice[dice_index]))
            dice_index += 1

        if len(moves) == 2:
            return moves


    return moves

if __name__ == "__main__":
    num_players = 1
    # the engine will run the ai for the player, with respect to its position in the list. So the first element (ai) will be run for the first player.
    ais = [ai]

    try:
        game = Game(num_players, ais)
        game.main()
    except KeyboardInterrupt:
        # Helps out with debugging
        print("\n")
        print(locked_pieces)
        print(unlocked_pieces)

        for piece in game.players[0].pieces:
            print(piece.position)
