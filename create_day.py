import os
from datetime import date

def create_day(day):
    folder_name = f"day{day:02d}"
    os.makedirs(folder_name, exist_ok=True)

    with open(f"{folder_name}/solution.py", "w") as f:
        f.write(f"# Solution for Day {day}\n\n")
        f.write("def main():\n")
        f.write("    # Your solution goes here\n")
        f.write("    pass\n\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    main()\n")
    
    with open(f"{folder_name}/input.txt", "w") as f:
        f.write("")  # Placeholder for input

    with open(f"{folder_name}/README.md", "w") as f:
        f.write(f"# Day {day}\n\n")
        f.write("## Problem Description\n\n")
        f.write("_Paste the problem description here._\n")

if __name__ == "__main__":
    today = date.today()
    day = today.day if today.month == 12 else 1
    create_day(day)
