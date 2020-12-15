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
    result = 0
    if source == max(source):
        result += 1
    elif 0 < num-n <= 3:
        n = num
    else:
        try:
            if 0 < source[i+1]-n <= 3:
                n = source[i+1]
                result += stepTwo(source[i+1:], n)
        except Exception:
            continue
        try:
            if 0 < source[source.index(num)+2]-n <= 3:
                n = source[i+2]
                result += stepTwo(source[i+2:], n)
        except Exception:
            continue
        pass

    return result


def main():
    filename = 'test'
    # filename = 'tests'
    # filename = 'input'
    with open(filename) as data:
        source = []
        for line in data:
            source.append(int(line.strip()))

        source.sort()
        # print(stepOne(source))
        result = 0
        for i, num in enumerate(source):
            result += stepTwo(source)

        print(result)


if __name__ == "__main__":
    main()
