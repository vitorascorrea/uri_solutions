def get_operations(N, F, values, index, current_sum, positive_values, negative_values, cache):
    if index >= N and current_sum == F:
        return True
    if index >= N and current_sum != F:
        return False

    if (index, current_sum) in cache:
        return cache[(index, current_sum)]

    in_ = get_operations(N, F, values, index + 1, current_sum + values[index], positive_values, negative_values, cache)
    out_ = get_operations(N, F, values, index + 1, current_sum - values[index], positive_values, negative_values, cache)

    if in_ and out_:
        positive_values[index] = True
        negative_values[index] = True
    elif in_ and not out_:
        positive_values[index] = True
    elif not in_ and out_:
        negative_values[index] = True

    has_result = in_ or out_
    cache[(index, current_sum)] = has_result

    return has_result


if __name__ == "__main__":
    test_cases = []

    while True:
        line_1 = list(map(int, input().split(" ")))
        N = line_1[0]
        F = line_1[1]

        if N == 0 and F == 0:
            break

        values = []
        for i in range(N):
            values.append(int(input()))

        test_cases.append({
            "N": N,
            "F": F,
            "values": values
        })

    for test_case in test_cases:
        positive_values = [None] * 40
        negative_values = [None] * 40
        cache = {}
        has_result = get_operations(test_case["N"], test_case["F"], test_case["values"], 0, 0, positive_values, negative_values, cache)

        if has_result:
            final_string = ""

            for i in range(len(test_case["values"])):
                if positive_values[i] and negative_values[i]:
                    final_string += "?"
                elif negative_values[i]:
                    final_string += "-"
                else:
                    final_string += "+"

            print(final_string)
        else:
            print("*")
