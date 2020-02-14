#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    """
    Write a function `reconstruct_trip` to reconstruct your trip from your mass of flight tickets. Each ticket is represented as a Class with the following form:

    where the `source` string represents the starting airport and the `destination` string represents the next airport along our trip. The ticket for your first flight has a destination with a `source` of `NONE`, and the ticket for your final flight has a `source` with a `destination` of `NONE`. 
    """

    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    route[0] = hash_table_retrieve(hashtable, "NONE")
    for i in range(1, length - 1):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route

    return route
