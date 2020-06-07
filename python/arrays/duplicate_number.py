from typing import List

def duplicate_number(array):
    for i in array:
        if array.count(i) > 1:
            return i

# Faster answer
def findDuplicate(self, nums: List[int]) -> int:
    res = []
    for i in nums:
        if i not in res:
            res.append(i)
        else:
            return i


def findDuplicate(self, nums: List[int]) -> int:
    for i in range(0, len(nums)):
        if nums[i] - 1 == 0:
            continue
        else:
            return nums[i]

# Only feasible if there number is duplicate only once and for one number
def findDuplicate(nums):
    current_sum = 0
    expected_sum = 0

    # Traverse the original array in the forward direction
    for num in nums:
        current_sum += num

    # Traverse from 0 to (length of array-1) to get the expected_sum
    # Alternatively, you can use the formula for sum of an Arithmetic Progression to get the expected_sum

    # The argument of range() functions are:
    # starting index [OPTIONAL], ending index (non exclusive), and the increment/decrement size [OPTIONAL]
    # It means that if the array length = n, loop will run form 0 to (n-2)
    for i in range(len(nums) - 1):
        expected_sum += i

    # The difference between the
    return current_sum - expected_sum

if __name__ == "__main__":
    print(findDuplicate([1, 3, 4, 2, 2]))
