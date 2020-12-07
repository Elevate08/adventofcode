import math


def treeFinder(slope, data):
    # Return count of trees run into during toboggan journey down slope
    i = -1 * slope[0]
    path = []
    for line in data[::slope[1]]:
        max = len(line)
        i += slope[0]
        if i >= max:
            i = i - max

        path.append(line[i])

    return path.count('#')


def main():
    filename = 'input'
    with open(filename) as data:
        map = []
        for line in data:
            map.append(str(line.rstrip('\n')))

    results = []
    for slope in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        results.append(treeFinder(slope, map))

    print(results)
    print(math.prod(results))


if __name__ == "__main__":
    print(main())
