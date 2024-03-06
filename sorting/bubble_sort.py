# сложность O(n^2)

def bubble_sort(collection: list[int]) -> list[int]:
    length = len(collection)
    for i in range(length):
        for j in range(length-i-1):
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
    return collection
