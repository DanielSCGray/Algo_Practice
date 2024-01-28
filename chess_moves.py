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

def all_safe_squares(queen: tuple):
    safe_squares = []
    for i in range(8):
        if i == queen[0]:
            continue
        for j in range(8):
            if j == queen[1]:
                continue
            if i + j == queen[0] + queen[1] or i - j == queen[0] - queen[1]: 
                continue
            safe_squares.append((i,j))
    return safe_squares

print(all_safe_squares((3,5)))
# [(0, 0), (0, 1), (0, 3), (0, 4), (0, 6), (0, 7), (1, 0), (1, 1), (1, 2), (1, 4), (1, 6), (2, 0), (2, 1), (2, 2), (2, 3), (2, 7), (4, 0), (4, 1), (4, 2), (4, 3), (4, 7), (5, 0), (5, 1), (5, 2), (5, 4), (5, 6), (6, 0), (6, 1), (6, 3), (6, 4), (6, 6), (6, 7), (7, 0), (7, 2), (7, 3), (7, 4), (7, 6), (7, 7)]






# Second-level challenge:​ accept an array of
# queens.

# my plan is to recursively merge the safe arrays accepting only shared safe squares

def safe_squares_list(queen_list):
    if len(queen_list) == 1:
        return all_safe_squares(queen_list[0])
    safe_squares = []
    my_queen = queen_list.pop()
    left = all_safe_squares(my_queen)
    right = safe_squares_list(queen_list)
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        left_square = left[left_idx]
        right_square = right[right_idx]
        if left_square == right_square:
            safe_squares.append(left_square)
            left_idx += 1
            right_idx += 1
        else:
            if left_square[0] > right_square[0]:
                right_idx += 1
            elif right_square[0] > left_square[0]:
                left_idx += 1
            else:
                if left_square[1] > right_square[1]:
                    right_idx += 1
                else:
                    left_idx += 1
    return safe_squares

print(safe_squares_list([(0,0), (1,3), (5,6)]))
# [(2, 1), (2, 5), (2, 7), (3, 2), (3, 7), (4, 1), (4, 2), (6, 1), (6, 2), (6, 4), (7, 1), (7, 2), (7, 5)]

# idea for alt solution: once i have the first safe square list I can just test each square vs each additional queen and reduce the list further

def alt_safe_squares(queen_list, safe_squares=None):
    if len(queen_list) == 0:
        return safe_squares
    if safe_squares == None:
        q = queen_list.pop()
        safe = all_safe_squares(q)
        return alt_safe_squares(queen_list, safe)
    queen = queen_list.pop()
    new_safe_s = []
    for move in safe_squares:
        if move[0] == queen[0] or move[1] == queen[1] or move[0] + move[1] == queen[0] + queen[1] or move[0] - move[1] == queen[0] - queen[1]:
            continue
        else:
            new_safe_s.append(move)
    return alt_safe_squares(queen_list, new_safe_s)

print(alt_safe_squares([(0,0), (1,3), (5,6)]))
# [(2, 1), (2, 5), (2, 7), (3, 2), (3, 7), (4, 1), (4, 2), (6, 1), (6, 2), (6, 4), (7, 1), (7, 2), (7, 5)] (same as above)


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
