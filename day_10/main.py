from collections import Counter


def stepOne(source):
    source.append(max(source)+3)
    difference = []
    n = 0
    while n != max(source):
        for num in source:
            difference.append(num-n)
            n = num

    return difference.count(1) * difference.count(3)


def stepTwo(source, n=0):
    source.append(source[-1] + 3)

    dp = Counter()
    dp[0] = 1

    for num in source:
        dp[num] = dp[num - 1] + dp[num - 2] + dp[num - 3]

    return dp[source[-1]]


def main():
    # filename = 'test'
    # filename = 'tests'
    filename = 'input'
    with open(filename) as data:
        source = []
        for line in data:
            source.append(int(line.strip()))

        source.sort()
        # print(stepOne(source))

        print(stepTwo(source))


if __name__ == "__main__":
    main()
