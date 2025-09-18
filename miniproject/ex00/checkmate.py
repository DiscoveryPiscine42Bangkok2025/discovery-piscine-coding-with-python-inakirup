def checkmate(board: str):
    lines = [line for line in board.splitlines() if line.strip() != ""]
    n = len(lines)

    king_pos = None
    for i in range(n):
        for j in range(n):
            if lines[i][j] == "K":
                king_pos = (i, j)
                break
        if king_pos:
            break
    if not king_pos:
        return

    ki, kj = king_pos

    def check_directions(directions, pieces):
        for di, dj in directions:
            x, y = ki + di, kj + dj
            while 0 <= x < n and 0 <= y < n:
                cell = lines[x][y]
                if cell != ".":
                    if cell in pieces:
                        return True
                    break
                x += di
                y += dj
        return False

    for dx, dy in [(1, -1), (1, 1)]:
        x, y = ki + dx, kj + dy
        if 0 <= x < n and 0 <= y < n and lines[x][y] == "P":
            print("Success")
            return

    if check_directions([(1,0),(-1,0),(0,1),(0,-1)], ["R","Q"]):
        print("Success")
        return

    if check_directions([(1,1),(1,-1),(-1,1),(-1,-1)], ["B","Q"]):
        print("Success")
        return

    print("Fail")