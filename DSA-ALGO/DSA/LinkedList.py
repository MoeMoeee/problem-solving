class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)

        if (self.head):
            current = self.head
            while current.next:
                current = current.next  # traverse through the LinkedList
            current.next = newNode  # insert node at the end after the traversal
        else:  # if no head -> insert the new node as the head
            self.head = newNode

    def remove(self, data):
        # TODO
        return

    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next  # move to next value


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    ll.insert(12)
    ll.insert(13)
    ll.insert(14)

    ll.printLinkedList()
