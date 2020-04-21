JMAX = "b"
JMIN = "w"
EMPTY = "#"

MAX_SCORE = 8 * 8

INITIAL_CONFIG = [
    # 0    #1   #2   #3   #4   #5   #6   #7   #8
    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "#", "#", "#", "#", "#", "#", "#", "#"],  # 1
    ["0", "#", "#", "#", "#", "#", "#", "#", "#"],  # 2
    ["0", "#", "#", "#", "#", "#", "#", "#", "#"],  # 3
    ["0", "#", "#", "#", "b", "w", "#", "#", "#"],  # 4
    ["0", "#", "#", "#", "w", "b", "#", "#", "#"],  # 5
    ["0", "#", "#", "#", "#", "#", "#", "#", "#"],  # 6
    ["0", "#", "#", "#", "#", "#", "#", "#", "#"],  # 7
    ["0", "#", "#", "#", "#", "#", "#", "#", "#"]  # 8
]

SMALL_CONFIG = [
    ["0", "0", "0", "0", "0"],
    ["0", "#", "#", "#", "#"],
    ["0", "#", "b", "w", "#"],
    ["0", "#", "w", "b", "#"],
    ["0", "#", "#", "#", "#"]
]

FINAL_CONFIG = [
    ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "w", "b", "b", "w", "b", "w", "b", "b"],  # 1
    ["0", "w", "b", "b", "w", "b", "w", "b", "b"],  # 1
    ["0", "w", "b", "b", "w", "b", "w", "b", "b"],  # 1
    ["0", "w", "b", "b", "w", "b", "w", "b", "b"],  # 1
    ["0", "w", "b", "b", "w", "b", "w", "b", "b"],  # 1
    ["0", "w", "b", "b", "w", "b", "w", "b", "b"],  # 1
    ["0", "w", "b", "b", "w", "b", "w", "b", "b"],  # 1
    ["0", "w", "b", "b", "w", "b", "w", "b", "b"],  # 1

]
