import itertools


def getList(data):

    try:
        return [int(x[0]) for x in data]
    except Exception:
        return [x for x in data]


def findSet(data, target, cont_num):
    n = len(data)
    count = start = 0
    curr_sum = data[0]
    index = 1
    i = 1
    while i <= n:
        if curr_sum == target and index == cont_num:
            contiguous_list = getList(data[start:i])
            count = min(contiguous_list) + max(contiguous_list)

        while index >= cont_num:
            curr_sum -= data[start]
            start += 1
            index = cont_num-1

        if i < n:
            curr_sum += data[i]
            index += 1
        i += 1

    return count


def stepOne(source, preamble, index=0):
    data = getList(source[index:preamble+index])
    for num in source[preamble+index:]:
        sums = [sum(values) for values in itertools.combinations(data, 2)]
        if int(num[0]) not in sums:
            return int(num[0])
        else:
            return stepOne(source, preamble, index+1)


def stepTwo(source, preamble, index=0):
    target = stepOne(source, preamble, index+1)
    source = getList(source)
    for n in range(0, len(source)):
        result = findSet(source, target, n)
        if result != 0:
            print(result)


def main():
    # filename = 'test'
    # preamble = 5
    filename = 'input'
    preamble = 25
    with open(filename) as data:
        source = []
        for line in data:
            source.append(line.strip().split())

        print(stepOne(source, preamble))
        stepTwo(source, preamble)


if __name__ == "__main__":
    main()
