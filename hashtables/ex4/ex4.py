def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}
    result = []
    for x in a:
        storage[x]=x
    for x in a:
        if x*-1 in storage and x > 0:
            result.append(x)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
