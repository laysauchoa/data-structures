
def add_one(array):
    return _add_one(array, carry_on=False)

# Solution with recursion
def _add_one(array:  List[int], carry_on: bool) -> List[int]:
    array_len = len(array)

    if array_len == 1 and array[0] == 9:
        return [1, 0]

    last_index = array_len - 1
    if array[last_index] != 9 and carry_on is False:
            array[last_index] += 1
            return array

    else:
        res = []
        carry_on = True
        res += _add_one(array[:last_index], carry_on) + [0]
    return res

# Solution with built-in python functions
def plusOne(self, digits: List[int]) -> List[int]:
    digits_plus_one = int(''.join(map(str, digits))) + 1
    lst_digits_plus_one = [int(x) for x in str(digits_plus_one)]
    return lst_digits_plus_one



if __name__ == "__main__":
    print(add_one([9, 9, 9]))
