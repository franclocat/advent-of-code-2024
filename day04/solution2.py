def main():
    grid = []
    with open("day04/input.txt", "r") as file:
        # Read the grid from the file, strip newlines, and store each line
        grid = [line.strip() for line in file]

    line_length = len(grid[0])  # Length of each row
    grid_height = len(grid)  # Height of the grid (number of rows)
    total_matches = 0  # Initialize the count of X-forms

    for row in range(1, grid_height - 1):
        for col in range(1, line_length - 1):
            # The center of the X must be 'A'
            if grid[row][col] == "A":
                if ((grid[row - 1][col - 1] == "M" and grid[row + 1][col + 1] == "S") or
                    (grid[row - 1][col - 1] == "S" and grid[row + 1][col + 1] == "M")) and \
                   ((grid[row - 1][col + 1] == "M" and grid[row + 1][col - 1] == "S") or
                    (grid[row - 1][col + 1] == "S" and grid[row + 1][col - 1] == "M")):
                    total_matches += 1

    print(f"Total X-forms: {total_matches}")

if __name__ == '__main__':
    main()
