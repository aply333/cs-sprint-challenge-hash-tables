def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}
    base = arrays[0]
    result = []
    for arr in arrays:
        subStorage = {}
        for i in arr:
            subStorage[i]=i
        storage[arrays.index(arr)] = subStorage
    for i in base:
        count = 0
        for x in storage:
            if i in storage[x]:
                count +=1
        if count >= len(storage):
            result.append(i)
    return result

# if __name__ == "__main__":
#     arrays = []

#     arrays.append( [1, 2, 3, 5, 8, 10])
#     arrays.append( [1, 2, 3, 14, 23, 48])
#     arrays.append( [1, 2, 3, 42, 56, 92])

#     print(intersection(arrays))

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
