def read_input(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    return lines


def list_input(input):
    result = list(input)

    return result


def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    xmas_positions = []

    # Helper function to check if "XMAS" or "SAMX" is in a given direction
    def check_direction(r, c, dr, dc):
        chars = []
        path = []
        for i in range(3):  # "MAS" has 4 letters
            nr, nc = r + dr * i, c + dc * i
            if 0 <= nr < rows and 0 <= nc < cols:
                chars.append(grid[nr][nc])
                if "A" == grid[nr][nc]:
                    path.append((nr, nc))
            else:
                return None, None
        found_string = "".join(chars)
        if found_string == "MAS":
            return "MAS", path
        # elif found_string == "SAMX":
        # return "SAMX"
        return None, None

    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check all 8 directions from the current cell
            directions = [
                # (0, 1),  # Right
                # (1, 0),  # Down
                (1, 1),  # Diagonal down-right
                (1, -1),  # Diagonal down-left
                # (0, -1),  # Left
                # (-1, 0),  # Up
                (-1, -1),  # Diagonal up-left
                (-1, 1),  # Diagonal up-right
            ]
            for dr, dc in directions:
                result, path = check_direction(r, c, dr, dc)
                if result:
                    xmas_positions.append(path)

    intersections = set()
    visited = {}
    for path in xmas_positions:
        for coord in path:
            if coord in visited:
                intersections.add(coord)
            else:
                visited[coord] = True

    return xmas_positions, intersections


def main():
    input = read_input("input")
    input = list_input(input)
    paths, intersections = find_xmas(input)
    print(len(intersections))


if __name__ == "__main__":
    main()
