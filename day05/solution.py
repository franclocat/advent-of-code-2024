# Solution for Day 5
def main():
    string = ""
    with open("day05\example.txt", "r") as file:
        for line in file:
            string += line
        rules_and_list = string.split("\n\n")
        rules = rules_and_list[0].split("\n")
        list = rules_and_list[1].strip().split(",")
        

if __name__ == '__main__':
    main()
