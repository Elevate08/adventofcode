def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines


def list_input(input):
    result = list(input)

    return result


def find_guard(grid):
    rows = len(grid)
    cols = len(grid[0])
    guards = ["^", ">", "<", "V"]
    for r in range(rows):
        for c in range(cols):
            for guard in guards:
                if guard == grid[r][c]:
                    guard, row, column = grid[r][c], r, c

    return guard, row, column


def move_guard(grid, guard, r, c):
    if guard == "^":
        if grid[r - 1][c] == "#":
            grid[r][c] = ">"
            return grid[r][c], r, c
        else:
            try:
                # Move guard up one row
                grid[r - 1][c] = "^"
                # Set guard original position to X
                grid[r][c] = "X"
                return grid[r - 1][c], r - 1, c
            except Exception as e:
                print(e)
                return grid[r][c], r, c
    elif guard == ">":
        if grid[r][c + 1] == "#":
            grid[r][c] = "V"
            return grid[r][c], r, c
        else:
            try:
                # Move guard to right
                grid[r][c + 1] = ">"
                # Set guard original position to X
                grid[r][c] = "X"
                return grid[r][c + 1], r, c + 1
            except Exception as e:
                print(e)
                return grid[r][c], r, c
    elif guard == "V":
        if grid[r + 1][c] == "#":
            grid[r][c] = "<"
            return grid[r][c], r, c
        else:
            try:
                # Move guard down
                grid[r + 1][c] = "V"
                # Set guard original position to X
                grid[r][c] = "X"
                return grid[r + 1][c], r + 1, c
            except Exception as e:
                print(e)
                return grid[r][c], r, c
    else:
        if grid[r][c - 1] == "#":
            grid[r][c] = "^"
            return grid[r][c], r, c
        else:
            try:
                # Move guard to left
                grid[r][c - 1] = "<"
                # Set guard original position to X
                grid[r][c] = "X"
                return grid[r][c - 1], r, c - 1
            except Exception as e:
                print(e)
                return grid[r][c], r, c


def navigate_map(grid):
    guard, r, c = find_guard(grid)

    for i in range(100):
        guard, r, c = move_guard(grid, guard, r, c)


def main():
    input = read_input("input")
    input = list_input(input)
    navigate_map(input)


if __name__ == "__main__":
    main()
