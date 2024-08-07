#  List Comprehensions

# 1
row = [WHITE_PAWN for i in range(8)] 

# 2
squares = [x ** 2 for x in range(10)]

# 3
twos = [2 ** i for i in range(8)]


# 4
odds = [x for x in squares if x % 2 != 0 ]
