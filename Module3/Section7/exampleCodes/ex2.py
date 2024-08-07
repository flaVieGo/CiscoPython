# Two-dimensional arrays

# 1
board = []
 
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row) 


# 2 - As list comprehensions can be nested, we can shorten the board creation in the following way:
board = [[EMPTY for i in range(8)] for j in range(8)] 