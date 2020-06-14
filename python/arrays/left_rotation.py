
def rotate(d, array):
    if array == [] or d == 0:
        return array
    d = d - 1
    array = array[1::] + [array[0]]
    return rotate(d, array)


