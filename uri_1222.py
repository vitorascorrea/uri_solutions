def count_pages(N, L, C, words):
    char_count = 0
    line_count = 1
    page_count = 1

    while len(words) > 0:
        word_len = len(words[0])

        if char_count + word_len <= C:
            should_add_space = (1 if char_count + word_len < C else 0)
            char_count += word_len + should_add_space
            words = words[1:]
        else:
            char_count = 0
            if line_count + 1 <= L:
                line_count += 1
            else:
                line_count = 1
                page_count += 1

    return page_count

if __name__ == "__main__":
    test_cases = []

    while True:
        try:
            line_1 = list(map(int, input().split(" ")))
            N = line_1[0]
            L = line_1[1]
            C = line_1[2]
            words = input().split(" ")

            test_cases.append({
                "N": N,
                "L": L,
                "C": C,
                "words": words
            })
        # except EOFError:
        except:
            break

    for test_case in test_cases:
        print(count_pages(test_case["N"], test_case["L"], test_case["C"], test_case["words"]))
