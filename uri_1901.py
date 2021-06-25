def count_butterflies(grid, coordinates):
    butterflies_map = {}

    for points in coordinates:
        species = grid[points[0] - 1][points[1] - 1]
        if not species in butterflies_map:
            butterflies_map[species] = True

    return len(butterflies_map.keys())

if __name__ == "__main__":
    N = int(input())
    grid = []
    coordinates = []

    for i in range(N):
        row = list(map(int, input().split(" ")))
        grid.append(row)

    for i in range(2 * N):
        points = list(map(int, input().split(" ")))
        coordinates.append(points)

    print(count_butterflies(grid, coordinates))
