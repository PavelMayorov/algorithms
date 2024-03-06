# сложность O(n(log(n)))

def quick_sort(collection: list[int]) -> list[int]:
    if len(collection) < 2:
        return collection
    central = collection[0]
    less = [element for element in collection[1:] if element < central]
    greater = [element for element in collection[1:] if element >= central]
    return quick_sort(less) + [central] + quick_sort(greater)
