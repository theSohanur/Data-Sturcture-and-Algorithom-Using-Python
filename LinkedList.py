class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_start(self, data):
        self.size += 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self, data):
        if self.head is None:
            return
        self.size -= 1
        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    # # O(1) type complexity
    def size(self):
        return self.size

    # # O(N) complexity
    def size2(self):
        actualNode = self.head
        size = 0
        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
        return size

    def insert_end(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode

    def traverse_node(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode.data, " ", end='')
            actualNode = actualNode.nextNode


n_list = LinkedList()
n_list.insert_start(5)
n_list.insert_start(4)
n_list.traverse_node()
print(n_list.size)
