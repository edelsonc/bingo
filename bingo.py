import sys
from random import shuffle

html_header = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            table th { border: 1px solid black }
        </style>
    </head>
    <body>
        <h1>Bingo time!</h1>
"""

html_footer = """
    </body>
</html>
"""


def create_check_item(choice):
    return "<input type=\"checkbox\" name=\"bingo\">{}".format(choice)


def create_row_element(row):
    formated_row = [ "<th>" + create_check_item(choice) + "</th>" for choice in row ]
    return "<tr>\n" + "\n".join(formated_row) + "</tr>\n"


def create_table(rows):
    # rows is a list of list, where each list is of the same length and
    # represents the rows of our bingo board
    formated_rows = [ create_row_element(row) for row in rows ]
    return "<table>\n" + "\n".join(formated_rows) + "</table>\n"


def create_rows(choices, n_cols=5):
    """
    Now we create a list of n rows
    """
    row = []
    rows = []
    for i, choice in enumerate(choices):
        row.append(choice)
        if (i + 1) % n_cols == 0:
            rows.append(row[:])
            row = []

    return rows


def create_board_order(choices, free):
    """Small function to shuffle choices and insert free space"""
    assert len(choices) == 24, "Board must be 5x5 for bingo!"
    
    board = choices[:]
    shuffle(board)
    board.insert(len(board) // 2, free)
    return board


if __name__ == "__main__":

    free = "free"
    try:
        with open("bingo_choices.txt", "r") as f:
            choices = [ i.strip() for i in f.readlines() if i.strip() != "" ]

    except FileNotFoundError:
        print("File `bingo_choices.txt` not found in local directory. Please make create a file of board choices")
        sys.exit(1)


    board_list = create_board_order(choices, free)
    rows = create_rows(board_list)
    table = create_table(rows)
    print( html_header + table + html_footer)

