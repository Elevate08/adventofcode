import re


def validate(data):
    # Character must be in the password x <= char =< y
    step_one_valid = 0
    step_two_valid = 0
    for line in data:
        line = re.compile("(-|:*\\s)").split(line)
        min = int(line[0])
        max = int(line[2])
        char = line[4]
        password = line[6]

        if password.count(char) in range(min, max+1):
            step_one_valid += 1

        match = 0
        for index in [min-1, max-1]:
            try:
                if char == password[index]:
                    match += 1
            except Exception:
                print(len(password))

        if match == 1:
            step_two_valid += 1

    return step_one_valid, step_two_valid


def main():
    with open('input') as data:
        print(validate(data))


if __name__ == "__main__":
    main()
