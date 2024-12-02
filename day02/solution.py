def is_safe(levels):
    if len(levels) < 2:
        return False

    increasing = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(-3 <= levels[i + 1] - levels[i] <= -1 for i in range(len(levels) - 1))
    return increasing or decreasing


def count_safe_reports_with_dampener(reports):
    safe_count = 0

    for report in reports:
        if is_safe(report):
            # Safe without removing any level
            safe_count += 1
        else:
            # Check if removing a single level makes it safe
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]
                if is_safe(modified_report):
                    safe_count += 1
                    break

    return safe_count

with open("day02\input.txt", "r") as f:
    reports = [list(map(int, line.split())) for line in f]

result = count_safe_reports_with_dampener(reports)
print(f"Number of safe reports: {result}")
