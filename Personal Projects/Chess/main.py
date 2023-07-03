import chess
import chess.svg

import webbrowser, os

PRINT_BOARD = True
USE_SAN = True

move_format = "SAN" if USE_SAN else "UCI"

board = chess.Board()

player = "White"

#r1b1k2r/ppppq1pp/2n1pn2/2b1P1B1/8/2N2N2/PPP2PPP/R2QKB1R w KQkq - 0 1

squares = {
	'a1': chess.A1,
	'a2': chess.A2,
	'a3': chess.A3,
	'a4': chess.A4,
	'a5': chess.A5,
	'a6': chess.A6,
	'a7': chess.A7,
	'a8': chess.A8,
	'b1': chess.B1,
	'b2': chess.B2,
	'b3': chess.B3,
	'b4': chess.B4,
	'b5': chess.B5,
	'b6': chess.B6,
	'b7': chess.B7,
	'b8': chess.B8,
	'c1': chess.C1,
	'c2': chess.C2,
	'c3': chess.C3,
	'c4': chess.C4,
	'c5': chess.C5,
	'c6': chess.C6,
	'c7': chess.C7,
	'c8': chess.C8,
	'd1': chess.D1,
	'd2': chess.D2,
	'd3': chess.D3,
	'd4': chess.D4,
	'd5': chess.D5,
	'd6': chess.D6,
	'd7': chess.D7,
	'd8': chess.D8,
	'e1': chess.E1,
	'e2': chess.E2,
	'e3': chess.E3,
	'e4': chess.E4,
	'e5': chess.E5,
	'e6': chess.E6,
	'e7': chess.E7,
	'e8': chess.E8,
	'f1': chess.F1,
	'f2': chess.F2,
	'f3': chess.F3,
	'f4': chess.F4,
	'f5': chess.F5,
	'f6': chess.F6,
	'f7': chess.F7,
	'f8': chess.F8,
	'g1': chess.G1,
	'g2': chess.G2,
	'g3': chess.G3,
	'g4': chess.G4,
	'g5': chess.G5,
	'g6': chess.G6,
	'g7': chess.G7,
	'g8': chess.G8,
	'h1': chess.H1,
	'h2': chess.H2,
	'h3': chess.H3,
	'h4': chess.H4,
	'h5': chess.H5,
	'h6': chess.H6,
	'h7': chess.H7,
	'h8': chess.H8
}

def GetMove():
    #print(player)
    move = input(f"Move to play ({move_format} format): ")

    try:
        if move.lower() == "takeback":
            return move.lower()
        if move.lower() == "resign":
            return move.lower()
        if move.lower() == "fen":
            return move.lower()

        return {
            "UCI": str(board.parse_san(move)) if USE_SAN else move,
            "SAN": move if USE_SAN else str(board.parse_uci(move))
        }
    except:
        return ""
def ShowBoard(lastmove):
    text = f"{player} to move"
    if board.is_game_over():
        text = "Game over"
    if board.is_checkmate():
        text = "Checkmate, " + ("White" if player == "Black" else "Black") + " won"
    if board.is_stalemate():
        text = "Stalemate! Draw..."
    if board.is_insufficient_material():
        text = "Insufficient material! Draw..."

    arrows = []
    if lastmove != "":
        arrows = [
            (
                squares[lastmove["UCI"][0:2]],
                squares[lastmove["UCI"][2:]],
            )
       ]
    svg_data = chess.svg.board(board, size=700, arrows=arrows) + f"""<h1 style="font-size: 70px; font-family: 'Arial'; padding-left: 20px">{text}</h1>"""
    """ Loads the svg data to the webpage """
    file = open("display.html", "w")
    file.write(svg_data)
    file.close()

    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('file://' + os.path.realpath("display.html"), 0, autoraise=False)


ShowBoard("")
if PRINT_BOARD: print(board)

while True:
    move = GetMove()
    if move == "":
        continue

    if move == "fen":
        fen = input("Input FEN: ")
        board.set_fen(fen)
        player = "White" if fen.split(" ")[1] == "w" else "Black"
        ShowBoard("")
        if PRINT_BOARD: print(board)
        continue
    if move == "takeback":
        board.pop()
        print("Took back move")
        player = "Black" if player == "White" else "White"
        ShowBoard("")
        if PRINT_BOARD: print(board)
        continue
    if move == "resign":
        print("Resigned!","White" if player == "Black" else "Black", "won!")
        break
    if chess.Move.from_uci(move["UCI"]) not in board.legal_moves:
        print("Illegal move!")
        continue
    if USE_SAN: 
        board.push_san(move["SAN"])
    else:
        board.push_uci(move["UCI"])
    move_ = move["SAN"] if USE_SAN else move["UCI"]
    print(f"Played move: {move_}")
    print("Current FEN:",board.board_fen)
    player = "Black" if player == "White" else "White"
    ShowBoard(move)
    if PRINT_BOARD: print(board)
    if board.is_checkmate():
        print("Checkmate!","White" if player == "Black" else "Black", "won!")
        break
    if board.is_stalemate():
        print("Stalemate! Draw...")
        break
    if board.is_insufficient_material():
        print("Insufficient material! Draw...")
        break
    if board.is_game_over():
        print("Game over")
        break
