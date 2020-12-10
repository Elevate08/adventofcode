def stepOne(source, n=0, visited=[], acc=0):
    while n <= len(source):
        for i in range(0, len(source)):
            if n in visited:
                print(acc)
                n += len(source)
                break
            else:
                visited.append(n)
                if source[n][0] == "acc":
                    if source[n][1][0] == "-":
                        acc -= int(source[n][1][1:])
                    elif source[n][1][0] == "+":
                        acc += int(source[n][1][1:])
                    n += 1
                elif source[n][0] == "jmp":
                    if source[n][1][0] == "-":
                        n -= int(source[n][1][1:])
                    elif source[n][1][0] == "+":
                        n += int(source[n][1][1:])
                else:
                    n += 1


def stepTwo(source, n=0, visited=[], acc=0):
    swap = True
    while n <= len(source):
        for i in range(0, len(source)):
            if n == len(source):
                n += len(source)
                return acc
            elif n in visited:
                visited = []
                n = 0
                acc = 0
                swap = True
            else:
                visited.append(n)
                if source[n][0] == "acc":
                    if source[n][1][0] == "-":
                        acc -= int(source[n][1][1:])
                    elif source[n][1][0] == "+":
                        acc += int(source[n][1][1:])
                    n += 1
                elif swap is True:
                    # Swap the action
                    if len(source[n]) < 3:
                        source[n].append("x")
                        swap = False
                        if source[n][0] == "jmp":
                            n += 1
                        elif source[n][0] == "nop":
                            if source[n][1][0] == "-":
                                if int(source[n][1][1:]) == 0:
                                    n -= 1
                                else:
                                    n -= int(source[n][1][1:])
                            elif source[n][1][0] == "+":
                                if int(source[n][1][1:]) == 0:
                                    n += 1
                                else:
                                    n += int(source[n][1][1:])
                    else:
                        if source[n][0] == "jmp":
                            if source[n][1][0] == "-":
                                n -= int(source[n][1][1:])
                            elif source[n][1][0] == "+":
                                n += int(source[n][1][1:])
                        else:
                            n += 1
                elif swap is False:
                    if source[n][0] == "jmp":
                        if source[n][1][0] == "-":
                            n -= int(source[n][1][1:])
                        elif source[n][1][0] == "+":
                            n += int(source[n][1][1:])
                    else:
                        n += 1

    return acc


def main():
    # filename = 'test'
    filename = 'input'
    with open(filename) as data:
        source = []
        for line in data:
            source.append(line.strip().split())

        # stepOne(source)
        print(stepTwo(source))


if __name__ == "__main__":
    main()
