
# exercise - chess
# Under the assumption of having only one solitary piece on the chessboard and moving
# white write a program that for a given chess piece (one of: pawn^, bishop, jumper,
# rook^, hetman^, king) and the coordinates of the position of this figure (as LC - Letter, Digit) will determine in
# how many ways this piece can move.

def count_moves(piece, position):
  # Convert the position to zero-based row and column indices
  row = int(position[1]) - 1
  col = ord(position[0]) - ord('A')
  # Define a dictionary of move counts for each piece
  move_counts = {
      "pawn": 2 if row > 0 else 1,  # Pawns can move forward one square, or capture diagonally
      "bishop": min(row, col) + min(row, 7 - col) + min(7 - row, col) + min(7 - row, 7 - col),  # Bishops can move diagonally in any direction
      "knight": 8 - (2 * (row < 1) + (col < 1)),  # Knights can move to any of the 8 squares around them
      "rook": row + (7 - row) + col + (7 - col),  # Rooks can move horizontally or vertically in any direction
      "queen": min(row, col) + min(row, 7 - col) + min(7 - row, col) + min(7 - row, 7 - col) + row + (7 - row) + col + (7 - col),  # Queens can move diagonally, horizontally, or vertically in any direction
      "king": 8 - (2 * (row < 1) + 2 * (row > 6) + 2 * (col < 1) + 2 * (col > 6)),  # Kings can move one square in any direction
  }
  # Return the count of moves for the given piece
  return move_counts[piece]

print(count_moves("king", "D4"))