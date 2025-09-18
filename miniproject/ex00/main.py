from checkmate import checkmate

def main():
    board1 = """\
R...
.K..
..B.
....\
"""

    board2 = """\
R...
.K..
....
....\
"""
    checkmate(board1)
    checkmate(board2)

if __name__ == "__main__":
    main()