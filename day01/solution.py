# Solution for Day 1

def main():
    list1 = []
    list2 = []
    total_diff = 0
    repetition_count = {}
    similarity = 0
    with  open("C:/Users/fralo/Desktop/advent-of-code-2024/day01/input.txt", "r") as file:
        for line in file:
            line_numbers = line.split()
            list1.append(line_numbers[0])
            list2.append(line_numbers[1])

            right_number = int(line_numbers[1])
            if right_number not in repetition_count:
                repetition_count[right_number] = 1
            else:
                repetition_count.update({right_number : repetition_count.get(right_number) + 1})
    for i in range (0, len(list1)):
        left_number = int(list1[i])
        if left_number in repetition_count:
            similarity += left_number * repetition_count.get(left_number)

    list1.sort()
    list2.sort()
    for i in range(0, len(list1)):
        total_diff += abs(int(list1[i]) - int(list2[i]))
    print("Total difference: ", total_diff)
    print("Similarity: ", similarity)


if __name__ == '__main__':
    main()
