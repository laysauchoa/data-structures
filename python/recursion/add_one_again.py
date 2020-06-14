
def add_one_again(digits):
    carry_on = True
    return _add_one_again(digits, carry_on)

def add_one_single_arr(digits):
    if digits[0] == 9:
        return [1, 0]
    if digits[0] < 9:
        return [digits[0] + 1]

def _add_one_again(digits, carry_on):
    len_digits = len(digits)

    if len_digits == 1:
        if carry_on:
            return add_one_single_arr(digits)
        else:
            return digits

    last_index = len_digits - 1
    res = []
    temp = digits[last_index]

    if carry_on:
        if digits[last_index] == 9:
            temp = 0
            carry_on = True
        elif digits[last_index] < 9:
            temp  += 1
            carry_on = False
    res = _add_one_again(digits[:last_index], carry_on) + [temp]
    return res


if __name__ == "__main__":
    print(add_one_again([8, 8, 5, 0, 5, 1, 9, 7]) == [8, 8, 5, 0, 5, 1, 9, 8])
