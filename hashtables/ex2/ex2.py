#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    storage = {}
    for ticket in tickets:
        if ticket.source == "NONE":
            route.append(ticket.destination)
        else:
            storage[ticket.source] = ticket.destination
    for x in storage:
        route.append(storage[route[len(route)-1]])

    print("--|Storage|--")
    print(storage)
    print("--|Route|--")
    print(route)
    return route

