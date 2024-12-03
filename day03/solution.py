import re

def scan_multiplication(segment):
    result = 0
    # Find all occurrences of `mul(a, b)`
    multiplications = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", segment)
    for a, b in multiplications:
        result += int(a) * int(b)
    return result

def filter_valid_segments(line):
    valid_segments = []
    parts = re.split(r"(don't|do)", line)
    skip = False

    for part in parts:
        if part == "don't":
            skip = True
        elif part == "do":
            skip = False
        elif not skip and part not in ("don't", "do"):
            valid_segments.append(part)
    
    return valid_segments

def main():
    total = 0
    with open("day03/input.txt", "r") as file:
        for line in file:
            # Get valid segments by filtering out ignored portions
            valid_segments = filter_valid_segments(line)
            for segment in valid_segments:
                # Compute and sum results from each segment
                total += scan_multiplication(segment)
    print(total)

if __name__ == '__main__':
    main()
