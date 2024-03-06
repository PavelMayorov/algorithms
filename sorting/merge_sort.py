# сложность O(n(log(n)))

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


def merge_sort(collection: list[int]) -> list[int]:
    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    left = merge_sort(collection[:mid])
    right = merge_sort(collection[mid:])
    return merge(left, right)
