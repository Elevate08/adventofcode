def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines


def list_input(input):
    result = list(input)

    return result


def navigate_map(grid):
    rows = len(grid)
    cols = len(grid[0])

    def find_guard():
        guards = ["^", ">", "<", "V"]
        for r in range(rows):
            for c in range(cols):
                for guard in guards:
                    if guard == grid[r][c]:
                        return grid[r][c], r, c

    def move_guard(r, c):
        if guard == "^":
            if grid[r - 1][c] == "#":
                grid[r][c] == ">"
                return r, c
            else:
                if grid[r - 1][c] != "." and grid[r - 1][c] != "X":
                    print(grid[r - 1][c])
                try:
                    # Move guard up one row
                    grid[r - 1][c] == guard
                    # Set guard original position to X
                    grid[r][c] == "X"
                    return r - 1, c
                except Exception as e:
                    print(e)
                    return False
        if guard == ">":
            if grid[r][c + 1] == "#":
                grid[r][c] == "V"
                return r, c
            else:
                if grid[r][c + 1] != "." or grid[r][c + 1] != "X":
                    print(grid[r][c + 1])
                try:
                    # Move guard to right
                    grid[r][c + 1] == guard
                    # Set guard original position to X
                    grid[r][c] == "X"
                    return r, c + 1
                except Exception as e:
                    print(e)
                    return False
        if guard == "V":
            if grid[r + 1][c] == "#":
                grid[r][c] == "V"
                return r, c
            else:
                if grid[r + 1][c] != "." or grid[r + 1][c] != "X":
                    print(grid[r + 1][c])
                try:
                    # Move guard down
                    grid[r + 1][c] == guard
                    # Set guard original position to X
                    grid[r][c] == "X"
                    return r + 1, c
                except Exception as e:
                    print(e)
                    return False
        if guard == "<":
            if grid[r][c - 1] == "#":
                grid[r][c] == "^"
                return r, c
            else:
                if grid[r][c - 1] != "." or grid[r][c - 1] != "X":
                    print(grid[r][c - 1])
                try:
                    # Move guard to left
                    grid[r][c - 1] == guard
                    # Set guard original position to X
                    grid[r][c] == "X"
                    return r, c - 1
                except Exception as e:
                    print(e)
                    return False

    guard, r, c = find_guard()

    for i in range(100):
        r, c = move_guard(r, c)


def main():
    input = read_input("input")
    input = list_input(input)
    navigate_map(input)


if __name__ == "__main__":
    main()
