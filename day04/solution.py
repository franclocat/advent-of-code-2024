import re
# Solution for Day 4
def main():
    grid = []
    with open("day04\input.txt", "r") as file:
        grid = [line.strip() for line in file]

    line_length = len(grid[0])
    grid_height = len(grid)
    total_matches = 0

    # Horizontal Matches
    for row in grid:
        total_matches += row.count("XMAS")
        total_matches += row.count("SAMX")

    # Vertical Matches
    for col in range(line_length):
        column_string = ''.join(grid[row][col] for row in range(grid_height))
        total_matches += column_string.count("XMAS")
        total_matches += column_string.count("SAMX")

    # Diagonal Downward Matches (\ direction)
    for start_row in range(grid_height - 3):  # Only consider rows where diagonal can fit
        for start_col in range(line_length - 3):  # Only consider columns where diagonal can fit
            diagonal = ''.join(grid[start_row + i][start_col + i] for i in range(4))
            if diagonal == "XMAS" or diagonal == "SAMX":
                total_matches += 1

    # Diagonal Upward Matches (/ direction)
    for start_row in range(3, grid_height):  # Only consider rows where diagonal can fit
        for start_col in range(line_length - 3):  # Only consider columns where diagonal can fit
            diagonal = ''.join(grid[start_row - i][start_col + i] for i in range(4))
            if diagonal == "XMAS" or diagonal == "SAMX":
                total_matches += 1

    print(total_matches)            
        
            


if __name__ == '__main__':
    main()
