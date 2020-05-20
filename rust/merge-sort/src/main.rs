pub fn merge_sorted_lists(left_list: Vec<u32>, right_list: Vec<u32>) -> Vec<u32> {
    let sorted_left_list = sort(left_list);
    let sorted_right_list = sort(right_list);
    let mut merged_list: Vec<u32> = Vec::new();
    let mut left_idx = 0;
    let mut right_idx = 0;

    while left_idx < sorted_left_list.len() && right_idx < sorted_right_list.len() {
        if sorted_left_list[left_idx] < sorted_right_list[right_idx] {
            merged_list.push(sorted_left_list[left_idx]);
            left_idx += 1;
        } else {
            merged_list.push(sorted_right_list[right_idx]);
            right_idx += 1;
        }
    }
    while left_idx < sorted_left_list.len() {
        merged_list.push(sorted_left_list[left_idx]);
        left_idx += 1;
    }
    while right_idx < sorted_right_list.len() {
        merged_list.push(sorted_right_list[right_idx]);
        right_idx += 1;
    }
    return merged_list;
}

pub fn sort(unsorted_list: Vec<u32>) -> Vec<u32> {
    if unsorted_list.len() < 2 {
        return (unsorted_list).clone();
    }
    let division_point = unsorted_list.len() / 2;

    return merge_sorted_lists(
        unsorted_list[0..division_point].to_vec(),
        unsorted_list[division_point..].to_vec(),
    );
}

    #[cfg(test)]
    mod tests {
        use crate::merge_sorted_lists;
        #[test]
        fn merge_two_small_lists() {
            let arr: Vec<u32> = vec![2, 1];
            let arr2: Vec<u32> = vec![6, 0];
            assert_eq!(merge_sorted_lists(arr, arr2), [0, 1, 2, 6]);
        }
        #[test]
        fn merge_with_empty_list() {
            let arr: Vec<u32> = vec![2, 1, 100];
            let arr2: Vec<u32> = vec![];
            assert_eq!(merge_sorted_lists(arr, arr2), [1, 2, 100]);
        }
        #[test]
        fn merge_two_lists() {
            let arr: Vec<u32> = vec![6, 7, 0, 10, 300];
            let arr2: Vec<u32> = vec![1, 2, 100, 9, 8];
            assert_eq!(
                merge_sorted_lists(arr, arr2),
                [0, 1, 2, 6, 7, 8, 9, 10, 100, 300]
            );
        }
    }

fn main() {
   
}
