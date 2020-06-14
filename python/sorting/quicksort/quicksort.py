def quicksort_hoare(A, lo, hi):
    if lo < hi:
        partition_border = partition_hoare(A, lo, hi)
        quicksort_hoare(A, lo, partition_border)
        quicksort_hoare(A, partition_border + 1, hi)


def partition_hoare(A, lo, hi):
    pivot = A[(hi + lo) // 2]
    i = lo
    j = hi
    while True:
        while A[i] < pivot:
            i = i + 1
        while A[j] > pivot:
            j = j - 1
        if i >= j:
            return j
        A[i], A[j] = A[j], A[i]
        i = i + 1
        j = j - 1


def quicksort_lomuto(A, lo, hi):
    print("q", A, lo, hi)
    if lo < hi:
        partition_border = partition_lomuto(A, lo, hi)
        quicksort_lomuto(A, lo, partition_border - 1)
        quicksort_lomuto(A, partition_border + 1, hi)


def partition_lomuto(A, lo, hi):
    print("p", A, lo, hi)
    pivot = A[hi]
    i = lo
    for j in range(lo, hi + 1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i = i + 1
    A[i], A[j] = A[j], A[i]
    print("ret i", i)
    return i


if __name__ == "__main__":
    import timeit
    arr = [5, 4, 1, 3, 2]
    start = timeit.default_timer()
    quicksort_lomuto(arr, 0, 4)
    stop = timeit.default_timer()
    time_lomuto = stop - start

    arr = [5, 4, 1, 3, 2]
    start = timeit.default_timer()
    quicksort_hoare(arr, 0, 4)
    stop = timeit.default_timer()
    time_hoare = stop - start

    print(
        f"Partition Lomuto takes {time_lomuto-time_hoare} more time to execute than Partition Hoare")

    # 5 4 1 3 2
    # hi 4
    # p 2
    # i 0
    # j 0 -> 4
    # j 1
    # j 2
    # 1 4 5 3 2
    # i 1
    # j 3
    # j 4
    # 1 2 5 3 4
    #
    # quicksort(A, lo, p - 1) - nothing
    # quicksort(A, p + 1, hi)
    #  1 2 5 3 4
    #  lo 2 hi 4
    #  pivot 4
    #  i 2
    #  j 2 -> 4
    #  j 3
    #  1 2 3 5 4
    #  i 3
    #  j 4
    #  1 2 3 4 5

