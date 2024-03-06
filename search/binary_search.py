# сложность O(log(n))

def binary_search(sorted_collection: list[int], target: int) -> int:
    left = 0
    right = len(sorted_collection) - 1
    while left <= right:
        mid = (right + left) // 2
        if sorted_collection[mid] < target:
            left = mid + 1
        elif sorted_collection[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1
