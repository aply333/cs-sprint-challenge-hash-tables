def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length == 2:
        if weights[0]+weights[1] == limit:
            return [1,0]
        else:
            pass
    storage = {}
    for i in weights:
        storage[i] = limit - i
    for x in storage:
        if storage[x] in storage:
            return([weights.index(storage[x]), weights.index(x)])
    return None


print(get_indices_of_item_weights([4,6,10,15,16], 5, 21))