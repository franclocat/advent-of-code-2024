# Solution for Day 2
def is_safe(line):
    levels = list(map(int, report.split()))
    # Check if the levels are either all increasing or all decreasing
    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    
    # Check if the differences are within the range [1, 3]
    valid_differences = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))
    
    # Return True only if both conditions are met
    return (is_increasing or is_decreasing) and valid_differences

def main():
    safe_count = 0
    with open("C:/Projects/advent-of-code-2024/day02/input.txt", "r") as file:
        for line in file:
            if is_safe(line.strip()):
                safe_count += 1
    print(f"Number of safe reports: {safe_count}")

if __name__ == '__main__':
    main()
