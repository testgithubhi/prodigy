def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_valid_move(grid, row, col, num):
    # Check if the number is not in the same row and column
    return (
        num not in grid[row] and
        num not in [grid[i][col] for i in range(9)] and
        num not in [grid[i][j] for i in range(row - row % 3, row - row % 3 + 3) for j in range(col - col % 3, col - col % 3 + 3)]
    )

def find_empty_location(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def solve_sudoku(grid):
    empty_location = find_empty_location(grid)

    if not empty_location:
        return True  # Puzzle is solved

    row, col = empty_location

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True  # Successfully solved

            grid[row][col] = 0  # Backtrack if the current assignment does not lead to a solution

    return False

def is_valid_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                original = grid[i][j]
                grid[i][j] = 0  # Temporarily remove the number to check validity
                if not is_valid_move(grid, i, j, original):
                    return False
                grid[i][j] = original  # Restore the original number
    return True

def generate_sudoku():
    # Generate a completed Sudoku puzzle
    puzzle = [[0] * 9 for _ in range(9)]
    solve_sudoku(puzzle)

    # Remove some numbers to create the puzzle
    for _ in range(40):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0

    return puzzle

if __name__ == "__main__":
    import random

    # Example unsolved Sudoku puzzle
    puzzle = generate_sudoku()

    print("Unsolved Sudoku Puzzle:")
    print_grid(puzzle)

    if solve_sudoku(puzzle) and is_valid_sudoku(puzzle):
        print("\nSolved Sudoku Puzzle:")
        print_grid(puzzle)
    else:
        print("No valid solution exists.")
