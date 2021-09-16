# Piece-wise function
# 3x - 5  (x > 1)
# f(x) =  x + 2   (-1 <= x <= 1)
# 5x + 3  (x < -1)


def piece_wise_func(x):
        if x > 1:
                return 3*x - 5
        if x >= -1:
                return x +2
        return 5*x+3 


# alternative
f = lambda x: 3*x-5 if x>1 else 5*x+3 if x < -1 else x+2

print(f(2))