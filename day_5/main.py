def main():
    filename = 'input'
    # filename = 'test'
    seatIDs = []
    with open(filename) as data:
        data = data.read()
        source = data.split('\n')
        for line in source:
            rows = range(0, 128)
            columns = range(0, 8)
            for char in line[:7]:
                if char == "F":
                    rows = rows[:len(rows)//2]
                    if len(rows) == 1:
                        rows = rows.start
                if char == "B":
                    rows = rows[len(rows)//2:]
                    if len(rows) == 1:
                        rows = rows.start

            for char in line[7:]:
                if char == "L":
                    columns = columns[:len(columns)//2]
                    if len(columns) == 1:
                        columns = columns.start
                if char == "R":
                    columns = columns[len(columns)//2:]
                    if len(columns) == 1:
                        columns = columns.start

            try:
                seatIDs.append(rows * 8 + columns)
            except Exception:
                pass

    print(max(seatIDs))  # Step 1, Locate Max Seat ID Value

    # Step 2, Locate seat from list of seatIDs
    for i in list(range(min(seatIDs), max(seatIDs) + 1)):
        if i + 1 in seatIDs and i - 1 in seatIDs:
            if i not in seatIDs:
                print(f'Your seat is: {i}')


if __name__ == "__main__":
    main()
