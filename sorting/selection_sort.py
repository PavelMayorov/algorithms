# сложность O(n^2)

def selection_sort(collection: list[int]) -> list[int]:
    length = len(collection)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if collection[j] < collection[min_index]:
                min_index = j
        if min_index != i:
            collection[i], collection[min_index] = collection[min_index], collection[i]
    return collection
