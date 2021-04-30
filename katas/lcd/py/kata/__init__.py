# Implement functions here
def template(arg):
    result = f"Doing something with {arg}"
    return result


DIGITS = [
    [  # 0
        [0, 1, 0],
        [1, 0, 1],
        [1, 1, 1],
    ],
    [  # 1
        [0, 0, 0],
        [0, 0, 1],
        [0, 0, 1],
    ],
    [  # 2
        [0, 1, 0],
        [0, 1, 1],
        [1, 1, 0],
    ],
    [  # 3
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 1],
    ],
    [  # 4
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 1],
    ],
    [  # 5
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 1],
    ],
    [  # 6
        [0, 1, 0],
        [1, 1, 0],
        [1, 1, 1],
    ],
    [  # 7
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 1],
    ],
    [  # 8
        [0, 1, 0],
        [1, 1, 1],
        [1, 1, 1],
    ],
    [  # 9
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 1],
    ],
]


def number_to_matrix(number):
    digits = str(number)
    result = []

    for digit in digits:
        result.append(DIGITS[int(digit)])

    return result


def matrix_to_LCD(matrix_list):
    pass


# Idea:
# #9
# [0, 1, 0], #2 -> ' _ '
# [1, 1, 1], #7 -> '|_|'
# [0, 1, 1], #1 -> ' _|'
# Change each line to bin then to dec and dec represents a string, e.g.
# 0 -> '   '
# 1 -> '  |'
# 2 -> ' _ '
# 3 -> ' _|'
# 4 -> '|  '
# Note: the upper line will never have bits 0 and 2 turned on.
