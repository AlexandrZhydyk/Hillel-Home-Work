
"""
For a given pair of a and b : Consider a Chess board of a × b squares.
Now, for each of the squares; Imagine a Queen standing on that square and compute
the number of squares under the queen's attack. Add all the numbers you get
for each of the a × b possible queen's position and return it.

Examples :
    For a = 2 and b
     = 2 : squaresUnderQueenAttack(2,2) => 12.
    For a = 2 and b
     = 3 : squaresUnderQueenAttack(2,3) => 26."""


def chessboard_squares_under_queen_attack(a, b):
    fields_under_attack = ((b-1) + (a-1)) * a * b
    min_dimen = a if a <= b else b
    for i in range(1, a+1):
        for j in range(1, b+1):
            for n in range(1, min_dimen):
                if i + n <= a and j + n <= b:
                    fields_under_attack += 1
                if 1 <= i - n and 1 <= j - n:
                    fields_under_attack += 1
                if 1 <= i - n and j + n <= b:
                    fields_under_attack += 1
                if i + n <= a and 1 <= j - n:
                    fields_under_attack += 1
    return fields_under_attack
