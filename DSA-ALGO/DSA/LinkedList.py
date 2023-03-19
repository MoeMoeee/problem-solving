
# prepend and append(insert at the front and end)       O(1)
# insert                                                O(n)
# find                                                  O(n)
# delete                                                O(n)


class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        newNode = Node(data)
        prev_head = self.head
        self.head = newNode
        newNode.next = prev_head  # the next value should be the previous head

    def append(self, data):
        newNode = Node(data)
        if (self.head):
            self.tail.next = newNode
            self.tail = newNode
        else:  # if none is in the list
            self.tail = newNode
            self.head = newNode

    def insert(self, data, index):  # insert any positions
        newNode = Node(data)

        if (self.head):
            current = self.head
            while current.next:
                current = current.next  # traverse through the LinkedList
            current.next = newNode  # insert node at the end after the traversal
            self.tail = newNode
        else:  # if no head -> insert the new node as the head
            self.tail = newNode
            self.head = newNode

    def remove(self, target):
        current = self.head
        pre_node = self.head

        if current.data == target:
            self.head = current.next
        else:
            while(current):
                if current.data == target:
                    pre_node.next = current.next
                    current.next = None
                    break
                if current.next is None:
                    print('Error')
                    break
                else:
                    pre_node = current
                    current = current.next

    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next  # move to next value


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)

    ll.printLinkedList()
