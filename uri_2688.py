# -*- coding: utf-8 -*-
import math

def get_best_spot(grid, height):
    candidate_spots = {}

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            cell = row[j]
            if (cell == "00" or cell == "0" or cell == "") and not is_in_corner(grid, i, j):
                candidate_spots[(i, j)] = {
                    "avg_height": get_avg_height(grid, i, j),
                    "dist": get_distance_to_entry(grid, i, j)
                }

    min_dist = 10000
    best_spot = None

    for coord in candidate_spots.keys():
        spot = candidate_spots[coord]
        if spot["avg_height"] <= height and spot["dist"] < min_dist:
            min_dist = spot["dist"]
            best_spot = coord

    return best_spot


def is_in_corner(grid, i, j):
    above = grid[i - 1][j]
    below = "99"
    if valid_index(i + 1):
        below = grid[i + 1][j]
    left = grid[i][j - 1]
    right = grid[i][j + 1]

    # left-top corner
    if right == "99" and above == "99":
        return True

    # left-bottom corner
    if right == "99" and below == "99":
        return True

    # right-top corner
    if left == "99" and above == "99":
        return True

    # right-bottom corner
    if left == "99" and below == "99":
        return True

    return False


def get_distance_to_entry(grid, i, j):
    queue = [
        {
            "coordinates": (0, 7),  # always the same starting point
            "dist": 0
        }
    ]
    visited = []

    while len(queue) > 0:
        current = queue.pop(0)

        if current["coordinates"] == (i, j):
            return current["dist"]

        visited.append(current["coordinates"])

        for neighbor_c in get_neighbors(grid, current["coordinates"][0], current["coordinates"][1]):
            neighbor = {
                "coordinates": neighbor_c,
                "dist": current["dist"] + 1
            }

            if not neighbor["coordinates"] in visited:
                queue.append(neighbor)

    return -1


def valid_index(index):
    return index >= 0 and index < 13


def get_neighbors(grid, i, j):
    neighbors = []
    valid_points = ["99", "00", "0"]

    try:
        if valid_index(i - 1) and valid_index(j) and grid[i - 1][j] in valid_points:
            neighbors.append((i - 1, j))
    except:
        pass

    try:
        if valid_index(i + 1) and valid_index(j) and grid[i + 1][j] in valid_points:
            neighbors.append((i + 1, j))
    except:
        pass

    try:
        if valid_index(i) and valid_index(j - 1) and grid[i][j - 1] in valid_points:
            neighbors.append((i, j - 1))
    except:
        pass

    try:
        if valid_index(i) and valid_index(j + 1) and grid[i][j + 1] in valid_points:
            neighbors.append((i, j + 1))
    except:
        pass

    return neighbors


def get_avg_height(grid, i, j):
    height_sum = 0
    height_count = 0
    invalid_points = ["99", "88", "77", "11"]

    try:
        if valid_index(i - 1) and valid_index(j) and not grid[i - 1][j] in invalid_points:
            height_sum += int(grid[i - 1][j])
            height_count += 1
    except:
        pass

    try:
        if valid_index(i + 1) and valid_index(j) and not grid[i + 1][j] in invalid_points:
            height_sum += int(grid[i + 1][j])
            height_count += 1
    except:
        pass

    try:
        if valid_index(i) and valid_index(j - 1) and not grid[i][j - 1] in invalid_points:
            height_sum += int(grid[i][j - 1])
            height_count += 1
    except:
        pass

    try:
        if valid_index(i) and valid_index(j + 1) and not grid[i][j + 1] in invalid_points:
            height_sum += int(grid[i][j + 1])
            height_count += 1
    except:
        pass

    return math.floor(height_sum / height_count if height_count > 0 else 0)


if __name__ == "__main__":
    grid_size = 13

    while True:
        try:
            grid = []
            height = int(input().strip())

            for i in range(grid_size):
                row = list(filter(lambda x: x, input().strip().split(" ")))
                grid.append(row)

            best_spot = get_best_spot(grid, height)
            print("linha > {} coluna > {}".format(best_spot[0] + 1, best_spot[1] + 1))
        except EOFError:
            break
