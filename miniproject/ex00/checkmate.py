def checkmate(board: str):
    if not isinstance(board, str):
        return  # Invalid input - print nothing

    # Parse and validate board
    lines = [line.strip() for line in board.splitlines() if line.strip()] # remove empty lines

    if not lines or any(len(line) != len(lines) for line in lines): # If not square
        return  # Invalid board - print nothing

    grid = [list(line) for line in lines]

    # Debug: print the board
    print("Board:")
    for row in grid:
        print(" ".join(row))

    n = len(grid)
    
    # Find the King
    king_pos = None
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 'K':
                king_pos = (r, c)
                # Debug: print the King's position
                # print(f"King found at: {king_pos}")
                break
        if king_pos:
            break
    
    if not king_pos:
        return  # No King found
    
    # Check if any piece can capture the King
    for r in range(n):
        for c in range(n):
            piece = grid[r][c]
            if piece == '.' or piece == 'K':
                continue
                
            if can_capture_king(grid, r, c, piece, king_pos):
                print("Success" + "\n")
                return
    
    print("Fail" + "\n")

def can_capture_king(grid, r, c, piece, king_pos):
    n = len(grid)
    
    # Define movement directions for each piece (dictionary of lists)
    directions = {
        'R': [(1,0), (-1,0), (0,1), (0,-1)],                   # Rook: S,N,E,W
        'B': [(1,1), (1,-1), (-1,1), (-1,-1)],                 # Bishop: diagonals(SE,SW,NE,NW)
        'Q': [(1,0), (-1,0), (0,1), (0,-1),                    # Queen: S,N,E,W + diagonals
              (1,1), (1,-1), (-1,1), (-1,-1)],
        'P': [(-1,1), (-1,-1)]                                 # Pawn: diagonal(NE, NW) forward only
    }
    
    if piece not in directions:
        return False
    
    for dr, dc in directions[piece]:
        # Debug: print the piece and direction being checked (before ray check)
        # print(f"Checking piece {piece} at {(r,c)} in direction {(dr,dc)}")
        # For pawns, only check one square diagonally
        if piece == 'P':
            nr, nc = r + dr, c + dc
            # print(f"Checking pawn at {(r,c)} moving to {(nr,nc)}")
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) == king_pos:
                return True
        else:
            # For other pieces, check along the ray until hitting something
            nr, nc = r + dr, c + dc
            while 0 <= nr < n and 0 <= nc < n:
                # print(f"Checking {piece} at {(r,c)} moving to {(nr,nc)}")
                if grid[nr][nc] != '.':  # Hit a piece
                    if (nr, nc) == king_pos:  # It's the King!
                        return True
                    break  # Hit something else, can't continue
                nr += dr
                nc += dc
    
    return False