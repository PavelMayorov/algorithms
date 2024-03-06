# сложность O(n)

def linear_search(collection, target):
    for i, value in enumerate(collection):
        if value == target:
            return i
    return -1
