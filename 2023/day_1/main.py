def readInput(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines


def sortInput(input):
    result = []
    for line in input:
        line = convertToInt(line)
        list_input = list(line)
        value = []
        for item in list_input:
            if item.isdigit():
                value.append(item)
        result.append(value)

    return result


def convertToInt(line):
    line = line.replace("eightwo", "82")
    line = line.replace("nineight", "98")
    line = line.replace("twone", "21")
    line = line.replace("on1e", "11")
    line = line.replace("sevenine", "79")
    line = line.replace("oneight", "18")
    line = line.replace("zero", "0")
    line = line.replace("one", "1")
    line = line.replace("two", "2")
    line = line.replace("three", "3")
    line = line.replace("four", "4")
    line = line.replace("five", "5")
    line = line.replace("six", "6")
    line = line.replace("seven", "7")
    line = line.replace("eight", "8")
    line = line.replace("nine", "9")

    return line


def calibration(input):
    sum = 0
    for row in input:
        value = str(row[0]) + str(row[-1])
        # print(f"{value} - {row}")
        sum += int(value)

    print(sum)
    return sum


def main():
    input = readInput("input")
    input = sortInput(input)
    calibration(input)


if __name__ == "__main__":
    main()
