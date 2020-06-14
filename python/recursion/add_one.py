
def add_one(digits):
    return _add_one(digits, carry_on=True)

# Solution with recursion
def _add_one(digits, carry_on):
    array_len = len(digits)
    print(array_len)
    print("digits", digits)

    if array_len == 1:
        if carry_on:
            if digits[0] == 9:
                return [1, 0]
            else:
                return [digits[0] + 1]
        return digits

    last_index = array_len - 1
    if digits[last_index] != 9 and carry_on:
            digits[last_index] += 1
            return digits

    else:
        res = []
        carry_on = True
        res += _add_one(digits[:last_index], carry_on) + [0]
    return res

# Solution with built-in python functions
def plusOne(self, digits):
    digits_plus_one = int(''.join(map(str, digits))) + 1
    lst_digits_plus_one = [int(x) for x in str(digits_plus_one)]
    return lst_digits_plus_one



if __name__ == "__main__":
    print(add_one([1, 9, 9]))
