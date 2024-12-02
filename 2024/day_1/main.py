def readInput(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines


def sortInput(input):
    left = []
    right = []
    for line in input:
        split_input = line.split()
        if len(split_input) > 0:
            left.append(int(split_input[0]))
            right.append(int(split_input[1]))

    left = sorted(left)
    right = sorted(right)
    return left, right


def determineDifference(left, right):
    difference = 0
    for i in range(len(left)):
        difference += abs(int(left[i]) - int(right[i]))
    print(difference)


def similarityScore(left, right):
    similarity_score = 0
    for i in left:
        if right.count(i) > 0:
            similarity_score += i * right.count(i)

    print(similarity_score)


def main():
    input = readInput("input")
    left, right = sortInput(input)
    # determineDifference(left, right)
    similarityScore(left, right)


if __name__ == "__main__":
    main()
