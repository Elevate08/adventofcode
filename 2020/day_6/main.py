class Group():
    def __init__(self):
        self.members = []

    def new_member(self, data):
        self.members.append(data)

    def valid_answers(self):
        for i, member in enumerate(self.members):
            if i == 0:
                source = sorted(list.copy(member))
                valid = list.copy(source)
            else:
                for letter in source:
                    if letter not in member:
                        try:
                            valid.remove(letter)
                        except Exception:
                            pass

        return valid


def getSeparated(data):
    result = []
    valid = []
    for row in data:
        try:
            for char in row:
                valid.append(char)
        except Exception:
            valid.append(row)

        if row == "\n\n":
            result.append(valid)
            valid = []

    return result


# Step 1, all unique characters
def stepOne(data):
    valid = []
    result = 0
    for line in data:
        if len(line) == 1:
            result += len(valid)
            valid = []
        else:
            for char in line[:-1]:
                if char not in valid:
                    valid.append(char)

    return result + len(valid)


def stepTwo(data):
    result = []
    group = Group()
    count = 0
    for line in data:
        if len(line) != 1:
            answers = []
            for character in line[:-1]:
                answers.append(character)
            group.new_member(answers)
        else:
            if '\n' in line:
                result.append(group)
                group = Group()

    result.append(group)

    for group in result:
        valid = group.valid_answers()
        count += len(valid)

    return count


def main():
    filename = 'input'
    # filename = 'testing'

    with open(filename) as data:
        file = data.readlines()
        print(stepOne(file))
        print(stepTwo(file))


if __name__ == "__main__":
    main()
