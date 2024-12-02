class Bag:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add_bags(self, bags):
        contents = self.get_contents()
        for content in contents:
            # QTY = content[0]
            # Name = content[1]
            for bag in bags:
                try:
                    if content[1] in bag.name:
                        for i in range(0, int(content[0])+1):
                            self.bags.append(bag)
                except Exception:
                    pass

    def get_gold_count(self, bags):
        for content in self.contents:
            if "shiny gold" in content[1]:
                return 1
            else:
                for bag in bags:
                    if bag.name in content[1]:
                        if bag.get_gold_count(bags):
                            return 1

    def total_bag_count(self, bags):
        total = 0
        for content in self.contents:
            num = int(content[0])
            print(content[1])
            for bag in bags:
                if bag.name in content[1]:
                    total += (num * bag.total_bag_count(bags)) + num

        return total


def stepOne(data):
    bags = []
    new = True
    for line in data:
        line = line.rstrip('\n').strip().split('bag')
        for word in line:
            word = word.lstrip('s contain|, ')
            if '.' not in word and new:
                # Create New Bag
                word = word.rstrip()
                bag = Bag(word)
                new = False
            elif '.' not in word and not new:
                word = word.rstrip().split(' ', 1)
                if len(word) != 1:
                    bag.contents.append(word)
            else:
                bags.append(bag)
                new = True

    count = 0
    for bag in bags:
        if bag.get_gold_count(bags):
            print(bag.name + " : Can hold a shiny gold bag")
            count += 1

    return count


def stepTwo(data):
    bags = []
    new = True
    for line in data:
        line = line.rstrip('\n').strip().split('bag')
        for word in line:
            word = word.lstrip('s contain|, ')
            if '.' not in word and new:
                # Create New Bag
                word = word.rstrip()
                bag = Bag(word)
                new = False
            elif '.' not in word and not new:
                word = word.rstrip().split(' ', 1)
                if len(word) != 1:
                    bag.contents.append(word)
            else:
                bags.append(bag)
                new = True

    for bag in bags:
        if bag.name == "hiny gold":
            return bag.total_bag_count(bags)


def main():
    filename = 'input'
    # filename = 'test'
    with open(filename) as data:
        file = data.readlines()

        # print(stepOne(file))
        print(stepTwo(file))



if __name__ == "__main__":
    main()
