def readInput(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines


def sortInput(input):
    reports = []
    for line in input:
        reports.append(line.split())

    return reports


def safetyRules(report):
    increasing = False
    status = True
    for i in range(len(report) - 1):
        if i == 0:
            if int(report[i]) < int(report[i + 1]):
                increasing = True
        if increasing:
            if 0 < int(report[i + 1]) - int(report[i]) <= 3:
                pass
            else:
                status = False
                break
        else:
            if 0 < int(report[i]) - int(report[i + 1]) <= 3:
                pass
            else:
                status = False
                break
    return status


def safetyCheck(reports):
    safe = []
    unsafe = []
    for report in reports:
        status = safetyRules(report)
        if status:
            safe.append(report)
        else:
            unsafe.append(report)

    print(len(safe))
    for report in unsafe:
        for i in range(len(report)):
            temp_report = report.copy()
            temp_report.pop(i)
            status = safetyRules(temp_report)
            if status:
                safe.append(report)
                break

    print(len(safe))
    return safe


def main():
    input = readInput("input")
    reports = sortInput(input)
    safetyCheck(reports)


if __name__ == "__main__":
    main()
