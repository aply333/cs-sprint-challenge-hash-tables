# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = {}
    result = []
    for x in files:  
        storage[x] = x
    for y in queries:
        if y in storage:
            print("yes")
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
