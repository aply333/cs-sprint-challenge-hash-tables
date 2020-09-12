# Your code here
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return "{self.value}"

class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_head(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def __str__(self):
        return "{self.head}"


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    print(len(files))
    storage = {}
    result = []
    for x in files:
        x_split = x.rsplit('/',1)[-1]
        new_node = Node(x)  
        if x_split in storage:
            storage[x_split].add_to_head(new_node)
        else:
            storage[x_split] = LinkedList()
            storage[x_split].add_to_head(new_node)
    for q in queries:
        if q in storage:
            current = storage[q].head
            while current != None:
                result.append(current.value)
                current = current.next
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/lib/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
