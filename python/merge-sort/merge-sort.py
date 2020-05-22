def merge_sort(items):
    """
    Function called recursively to break down an
    input list to smaller, more manageable pieces in order
    to return an ordered list.

    This function works as the follows:
    1) splitting the original list into smaller sorted lists
    recursively until there is only 1 element in the list,

    2) merging back the presorted 1-element lists into 2-element
    lists, 4-element lists, and so on recursively.


    Args:
        items (list): List to be sorted.

    Returns:
        list: Ordered list from ascending order

    .. _Merge-Sort:
        https://www.geeksforgeeks.org/merge-sort/

    """
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    This is a helper function for `merge_sort` function.
    The merging portion is iterative and takes 2 sublists.

    The first element of the left sublist is compared to the first element of the right sublist.
    If it is smaller, it is added to a new sorted list, and removed from the left sublist.

    If it is bigger, the first element of the right sublist is added instead to the sorted list
    and then removed from the right sublist.
    This is repeated until either the left or right sublist is empty.

    The remaining non-empty sublist is appended to the sorted list.

      Args:
          left (list): List of left elements from original list.
          right (list): List of right elements from original list.

      Returns:
          list: ordered list

      """

    result = []

    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result


unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19,
                   202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]
ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print(
    f"Ordered list\n Ordered list1: {ordered_list1} \n Ordered list1: {ordered_list2} \n Ordered list3: {ordered_list3}")
