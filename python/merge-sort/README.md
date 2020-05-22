Merge Sort Merging
===================

Merge Sort is a divide and conquer algorithm. It consists of two parts:

* 1) splitting the original list into smaller sorted lists recursively until there is only 1 element in the list,
* 2) merging back the presorted 1-element lists into 2-element lists, 4-element lists, and so on recursively.

The merging portion is iterative and takes 2 sublists. The first element of the left sublist is compared to the first element of the right sublist. If it is smaller, it is added to a new sorted list, and removed from the left sublist. 

If it is bigger, the first element of the right sublist is added instead to the sorted list and then removed from the right sublist. This is repeated until either the left or right sublist is empty. The remaining non-empty sublist is appended to the sorted list.

Big-O Runtime for Merge Sort
----------------------------

The Merge Sort algorithm is divided into two parts. The first part repeatedly splits the input list into smaller lists to eventually produce single-element lists. The best, worst and average runtime for this part is Θ(log N). The second part repeatedly merges and sorts the single-element lists to twice its size until the original input size is achieved. The best, worst and average runtime for this part is Θ(N). Therefore, the combined runtime is Θ(N log N).
