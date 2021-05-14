# Implement functions here
def template(arg):
    result = f"Doing something with {arg}"
    return result


DIGITS = [
    [  # 0
        [0, 1, 0],  # 2
        [1, 0, 1],  # 5
        [1, 1, 1],  # 7
    ],
    [  # 1
        [0, 0, 0],  # 0
        [0, 0, 1],  # 1
        [0, 0, 1],  # 1
    ],
    [  # 2
        [0, 1, 0],  # 2
        [0, 1, 1],  # 3
        [1, 1, 0],  # 5
    ],
    [  # 3
        [0, 1, 0],  # 2
        [0, 1, 1],  # 3
        [0, 1, 1],  # 3
    ],
    [  # 4
        [0, 0, 0],  # 0
        [1, 1, 1],  # 7
        [0, 0, 1],  # 1
    ],
    [  # 5
        [0, 1, 0],  # 2
        [1, 1, 0],  # 6
        [0, 1, 1],  # 3
    ],
    [  # 6
        [0, 1, 0],  # 2
        [1, 1, 0],  # 6
        [1, 1, 1],  # 7
    ],
    [  # 7
        [0, 1, 0],  # 2
        [0, 0, 1],  # 1
        [0, 0, 1],  # 1
    ],
    [  # 8
        [0, 1, 0],  # 2
        [1, 1, 1],  # 7
        [1, 1, 1],  # 7
    ],
    [  # 9
        [0, 1, 0],  # 2
        [1, 1, 1],  # 7
        [0, 1, 1],  # 3
    ],
]


encoding = [
    [2, 5, 7],  # 0
    [0, 1, 1],  # 1
    [2, 3, 6],  # 2
    [2, 3, 3],  # 3
    [0, 7, 1],  # 4
    [2, 6, 3],  # 5
    [2, 6, 7],  # 6
    [2, 1, 1],  # 7
    [2, 7, 7],  # 8
    [2, 7, 3],  # 9
]

lcd = [
    "   ",  # 0
    "  |",  # 1
    " _ ",  # 2
    " _|",  # 3
    "|  ",  # 4
    "| |",  # 5
    "|_ ",  # 6
    "|_|",  # 7
]


def number_to_lcd(number):
    result = []
    digits = str(number)  # '18'

    line_top = ""
    line_mid = ""
    line_bot = ""
    for digit in digits:  # '1', '8'
        enc = encoding[int(digit)]
        line_top += lcd[enc[0]]  # '    _ '
        line_mid += lcd[enc[1]]  # '  ||_|'
        line_bot += lcd[enc[2]]  # '  ||_|'

    return "\n".join([line_top, line_mid, line_bot])


# Idea:
# #9
# [0, 1, 0], #2 -> ' _ '
# [1, 1, 1], #7 -> '|_|'
# [0, 1, 1], #3 -> ' _|'

# Idea 2:
# number_to_encoding
# #9: [2, 7, 3]
# encoding_to_string
# 2 -> ' _ '

# Change each line to bin then to dec and dec represents a string, e.g.
# 0 -> '   '
# 1 -> '  |'
# 2 -> ' _ '
# 3 -> ' _|'
# 4 -> '|  '
# 5 -> '| |'
# 6 -> '|_ '
# 7 -> '|_|'
# Note: the upper line will never have bits 0 and 2 turned on.
