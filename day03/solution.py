import re
# Solution for Day 3
def scanMultiplication(file):
    result = 0
    for line in file:
           multiplications = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
           for mult in multiplications:
               nums_in_mult = re.findall("\d{1,3}", mult)
               result += int(nums_in_mult[0]) * int(nums_in_mult[1])
    return result

def main():
    with open("day03\input.txt", "r") as file:
        result = scanMultiplication(file)
    print(result)
    

if __name__ == '__main__':
    main()
