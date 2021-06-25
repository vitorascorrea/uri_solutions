
def find_stacks(matrix, num_rocks, num_stacks):
    if matrix[num_rocks][num_stacks] == -1:
        matrix[num_rocks][num_stacks] = find_stacks(matrix, num_rocks, num_stacks - 1)
        if num_rocks >= num_stacks:
            matrix[num_rocks][num_stacks] += find_stacks(matrix, num_rocks - num_stacks, num_stacks)

    return matrix[num_rocks][num_stacks]


if __name__ == "__main__":
    num_rocks = int(input())
    matrix = [([-1] * (num_rocks + 1)) for i in range(num_rocks + 1)]

    valid_stacks = 0

    matrix[0][0] = 1

    for i in range(1, num_rocks + 1):
        matrix[i][0] = 0

    for i in range(1 - num_rocks % 2, num_rocks + 1, 2):
        valid_stacks += find_stacks(matrix, num_rocks - i, i)

    print(valid_stacks % ((10**9) + 7))
