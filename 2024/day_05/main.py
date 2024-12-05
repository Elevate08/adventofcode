def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
        orderingRules = []
        updates = []
        rules = True
        for line in lines:
            if "\n" == line:
                rules = False
            elif rules:
                orderingRules.append(line.strip())
            else:
                updates.append(line.strip())

    return orderingRules, updates


def process_updates(rules, updates):
    validUpdates = []
    invalidUpdates = []
    for update in updates:
        update = update.split(",")
        valid = True
        for rule in rules:
            rule = rule.split("|")
            if valid:
                # Determine if both numbers from rule are in update
                if int(update.count(rule[0])) > 0 and int(update.count(rule[1])) > 0:
                    # Check if first rule is before second rule
                    if int(update.index(rule[0])) < int(update.index(rule[1])):
                        valid = True
                    # Update is invalid
                    else:
                        valid = False

        if valid:
            validUpdates.append(update)
        else:
            invalidUpdates.append(update)

    return validUpdates, invalidUpdates


def final_calculation(valid_updates):
    sum = 0
    for update in valid_updates:
        length = len(update)
        if length % 2 != 0:
            middle_index = length // 2
            sum += int(update[middle_index])
        else:
            middle_index = length // 2 - 1
            sum += int(update[middle_index])

    return sum


def sort_invalid_updates(invalidUpdates, rules):
    for i in range(3):
        for update in invalidUpdates:
            for rule in rules:
                rule = rule.split("|")
                # Determine if both numbers from rule are in update
                if int(update.count(rule[0])) > 0 and int(update.count(rule[1])) > 0:
                    if update.index(rule[0]) < update.index(rule[1]):
                        pass
                    else:
                        update.insert(
                            update.index(rule[0]), update.pop(update.index(rule[1]))
                        )

    return invalidUpdates


def main():
    rules, updates = read_input("input")
    validUpdates, invalidUpdates = process_updates(rules, updates)
    finalCalculation = final_calculation(validUpdates)

    # print(finalCalculation)

    invalidUpdates = sort_invalid_updates(invalidUpdates, rules)
    # invalidUpdates = sort_invalid_updates(invalidUpdates, rules)
    # invalidUpdates = sort_invalid_updates(invalidUpdates, rules)
    invalidUpdatesSum = final_calculation(invalidUpdates)

    print(invalidUpdatesSum)


if __name__ == "__main__":
    main()
