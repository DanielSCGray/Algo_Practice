# IsChessMoveSafe
# Return if a chessboard square is threatened.
# isChessMoveSafe(intendedMove,queen)
# accepts an object indicating the location to check,
# and object of same type indicating location of an
# opposing queen.


def is_safe(move: tuple, queen: tuple):
    if move[0] == queen[0] or move[1] == queen[1]:
        return False
    #determine relative position:
    is_north = move[1] > queen[1]
    is_east = move[0] > queen[0]
    #explore relevant direction:
    queen_row = queen[0]
    queen_col = queen[1]
    if is_north:
        if is_east:
            while queen_row < 8 and queen_col < 8:
                if move[0] == queen_row and move[1] == queen_col:
                    return False
                queen_row += 1
                queen_col += 1
        else: 
            while queen_row >= 0 and queen_col < 8:
                if move[0] == queen_row and move[1] == queen_col:
                    return False
                queen_row -= 1
                queen_col += 1
    else:
        if is_east:
            while queen_row < 8 and queen_col >= 0:
                if move[0] == queen_row and move[1] == queen_col:
                    return False
                queen_row += 1
                queen_col -= 1
        else:
            while queen_row >= 0 and queen_col >= 0:
                if move[0] == queen_row and move[1] == queen_col:
                    return False
                queen_row -= 1
                queen_col -= 1
    return True

print(is_safe((0,0), (8,8)))
# False
print(is_safe((0,0), (8,6)))
# True

# Second-level challenge:​ accept an array of
# queens.

def is_safe_array(move: tuple, queen_list: list):
    if len(queen_list) == 0:
        return True
    my_queen = queen_list.pop()
    result = is_safe(move, my_queen)
    if result == False:
        return False
    return is_safe_array(move, queen_list)

print(is_safe_array((0,0), [(8,6), (8,7), (8,8)]))
# False
print(is_safe_array((0,0), [(8,6), (8,7), (5,4)]))
# True
print(is_safe_array((0,0), [(8,6), (8,8), (8,0)]))
# False

def is_safe_simplified(move: tuple, queen: tuple):
    if move[0] == queen[0] or move[1] == queen[1] or move[0] + move[1] == queen[0] + queen[1] or move[0] - move[1] == queen[0] - queen[1]:
        return False
    return True

print(is_safe_simplified((0,0), (7,7)))
#False
# AllSafeChessSquares
# Build on your solution to the previous challenge,
# to create allSafeChessSquares(queen)​ that
# returns all chessboard squares not threatened by
# a given queen.
# Second-level challenge:​ accept an array of
# queens.




# Eight Queens
# Build on previous solutions to write
# eightQueens()​. Return all arrangements of
# eight queens on an 8x8 chessboard, so that no
# queen threatens any other. What is the best way
# to return these results?
# Second:​ write a helper function that displays the
# results returned, using console.log().



# N Queens
# Generalize eightQueens()​ into a function
# nQueens(n,xSize,ySize)​ returning all
# arrangements of N unthreatened queens on an X
# x Y rectangular board. That is, eightQueens()
# == nQueens(8,8,8)​.
