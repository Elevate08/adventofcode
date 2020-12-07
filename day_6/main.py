# Step 1, all unique characters
def yesFinder(data):
    unique = []
    steptwo = []
    result_1 = 0
    result_2 = 0
    for line in data:
        if len(line) == 1:
            result_1 += len(unique)
            result_2 += len(steptwo)
            unique = []
            steptwo = []
        else:
            for char in line[:-1]:
                if char not in unique:
                    unique.append(char)

            if len(steptwo) == 0:
                steptwo.append(line)
            else:
                for char in steptwo:
                    if char not in line:
                        steptwo.remove(char)

    return result_1 + len(unique), result_2 + len(steptwo)


def main():
    # filename = 'input'
    filename = 'test'
    result = 0
    with open(filename) as data:
        result = yesFinder(data)
    print(result)


if __name__ == "__main__":
    main()
