import re


def readInput(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines


def listInput(input):
    instructions = list(input)

    return instructions


def repairInstructions(instructions):
    results = []
    for instruction in instructions:
        valid_instructions = re.findall(
            "(do[(][)]|don't[(][)]|mul[(][0-9]{,3},[0-9]{,3}[)])", instruction
        )
        results = results + valid_instructions

    return results


def processInstructions(instructions):
    enabled = True
    sum = 0
    for instruction in instructions:
        if "do()" == instruction:
            enabled = True
        elif "don't()" == instruction:
            enabled = False
        elif enabled:
            index = instruction.index(",")
            try:
                sum += int(instruction[4:index]) * int(instruction[index + 1 : -1])
            except:
                print(f"{instruction[4:index]} * {instruction[index + 1 : -1]}")
                print(instruction)

    print(sum)
    return sum


def main():
    input = readInput("input")
    instructions = listInput(input)
    instructions = repairInstructions(instructions)
    processInstructions(instructions)


if __name__ == "__main__":
    main()
