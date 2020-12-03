# Source
# https://stackoverflow.com/questions/49761846/how-to-sum-two-numbers-in-a-list

import itertools

def main():
    with open('input') as data:
        numbers = []
        target = 2020
        for line in data:
            numbers.append(int(line.rstrip('\n')))
        
        # Find two values from provided input whose sum equals 2020, multiply those values together
        for num in itertools.combinations(numbers,2):
            if sum(num) == target:
                return num[0] * num[1]
        # Find three values from provided input whose sum equals 2020, multiply those values together
        for num in itertools.combinations(numbers,3):
            if sum(num) == target:
                return num[0] * num[1] * num[2]


if __name__ == "__main__":
    print(main())
