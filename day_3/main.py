def main():
    with open('input') as data:
        map = []
        for line in data:
            map.append(str(line.rstrip('\n')))
        
        trees = 0
        down = 1
        right = 2
        path = []
        for line in map[::down]:
            try:
                path.append(line[right])
                right += 3
            except Exception as e:
                right = right - len(line)
                path.append(line[right])
                right += 3

        print(path)

        print(path.count('#'))


if __name__ == "__main__":
    print(main())
