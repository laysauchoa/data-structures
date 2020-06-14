
""" def minimumBribes(q):
    len_q = len(q)

    def is_chaotic(i, q):
        value_position = i + 1
        if q[i] - value_position >= 3:
            return True
    count = 0

    for i in range(0, len_q):
        if is_chaotic(i, q):
            return "Too chaotic"

        current_value = q[len_q - (i + 1)]
        for k in range(0, len_q - (i + 1)):
            value_to_compare = q[len_q - (i + 2 + k)]
            if current_value < value_to_compare:
                count += 1
    return count """


def minimumBribes(q):
    len_q = len(q)

    def is_chaotic(current):
        value_position = i + 1
        if current - value_position >= 3:
            return True

    def is_sorted(i, q):
        value_position = i
        if q[i] == value_position:
            return True

    bribes = 0
    count_sort = 0
    for i in range(0, len_q):

        if is_chaotic(q[i]):
            return "Too chaotic"

        if is_sorted(i, q):
            count_sort += 1

        if count_sort == len_q:
            break

        current_value = q[i]  # current_value = 2

        for k in range(max(current_value-2, 0), i):
            if current_value < q[k]:
                bribes += 1
    return bribes


if __name__ == "__main__":

    example = [2, 1, 5, 3, 4]
    print(minimumBribes(example))


