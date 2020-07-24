# # Node class to be used by multiple data structures
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.prev = None
#         self.next = None
#
#
# # Doubly Linked List class that will be used in future projects
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def __len__(self):
#         length = 0
#         node = self.head
#
#         while node != None:
#             length += 1
#             node = node.next
#
#         return length
#
#     def __repr__(self):
#         print_list = []
#         node = self.head
#
#         while node != None:
#             print_list.append(node.value)
#             node = node.next
#
#         return f"Contains: {print_list}"
#
#     # adds node to end of linked list
#     def add(self, node):
#         # checks to see if any nodes exist yet
#         if self.head == None and self.tail == None:
#             self.head = node
#             self.tail = node
#             node.prev = None
#             node.next = None
#         else:
#             node.next = None
#             node.prev = self.tail
#             self.tail.next = node
#             self.tail = node
#
#     def viewList(self):
#         node = self.head
#
#         while node != None:
#             print(node.value)
#             node = node.next
#
#     def peek(self):
#         return (self.head.value, self.tail.value)
#
#     def remove(self, node):
#         if node == self.head and node == self.tail:
#             self.head = None
#             self.tail = None
#         elif node == self.head:
#             self.head = node.next
#             node.next.prev = None
#         elif node == self.tail:
#             self.tail = node.prev
#             node.prev.next = None
#         else:
#             node.prev.next = node.next
#             node.next.prev = node.prev
#
#         node.next = None
#         node.prev = None
#
#     def addBefore(self, node, nodeToAdd):
#         nodeToAdd.next = node
#         nodeToAdd.prev = node.prev
#
#         if node == self.head:
#             self.head = nodeToAdd
#             node.prev = nodeToAdd
#         else:
#             node.prev.next = nodeToAdd
#             node.prev = nodeToAdd
#
#     def addAfter(self, node, nodeToAdd):
#         nodeToAdd.next = node.next
#         nodeToAdd.prev = node
#
#         if node == self.tail:
#             self.tail = nodeToAdd
#             node.next = nodeToAdd
#         else:
#             node.next.prev = nodeToAdd
#             node.next = nodeToAdd
#
#     def containsNodeWithValue(self, value):
#         node = self.head
#
#         while node != None and node.value != value:
#             node = node.next
#         return node != None
#
#     def removeNodeWithValue(self, value):
#         node = self.head
#
#         while node != None and node.value != value:
#             node = node.next
#         if node == None:
#             return
#         else:
#             self.remove(node)
#
#
# # doubleList = DoublyLinkedList()
# #
# # # doubleList.add(5)
# # # doubleList.add(43)
# # print(doubleList.viewList())
# # doubleList.add(45)

#####################################################################################

class Node(object):
    nextP = None
    prev = None

    def __init__(self, data):
        self.data = data
        Node.nextP = None
        Node.prev = None


class DLL(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    # Insert a node into the Linked List
    def insertNode(self, x):

        if self.head is None:
            n = Node(x)
            self.head = n
            self.tail = n

        else:
            n = Node(x)
            self.tail.nextP = n
            n.prev = self.tail
            self.tail = self.tail.nextP
            self.tail.nextP = None

        self.size += 1

    # Find a node from its integer value
    def findNode(self, x):
        if self.head.data == x:
            print(self.head)
            return self.head
        elif self.tail.data == x:
            print(self.tail)
            return self.tail

        else:
            iterator = self.head.nextP
            while iterator.nextP is not None:
                if iterator.data == x:
                    print(iterator)
                    return iterator
                else:
                    iterator = iterator.nextP

        return None

    # Delete a node based on the value
    def deleteNode(self, x):
        if self.head.data == x:
            self.head = self.head.nextP
            self.head.prev = None
            return self.head
        elif self.tail.data == x:
            self.tail = self.tail.prev
            self.tail.nextP = None
            return self.tail

        else:
            iterator = self.head.nextP
            while iterator.nextP is not None:
                if iterator.data == x:
                    iterator.prev.nextP = iterator.nextP
                    iterator.nextP.prev = iterator.prev
                    return iterator

                else:
                    iterator = iterator.nextP

        return None

    # After the first occurrence of Node with value x, insert a node with value y
    def insertAfter(self, x, y):
        if self.head.data == x:
            n = Node(y)
            self.head.nextP = n.nextP
            self.head.nextP.prev = n
            n.prev = self.head
            self.head.nextP = n

        elif self.tail.data == x:
            n = Node(y)
            self.tail.nextP = n
            n.prev = self.tail
            n.nextP = None
            self.tail = n

        else:
            iterator = self.head.nextP
            while iterator.nextP is not None:
                if iterator.data == x:
                    n = Node(y)
                    n.nextP = iterator.nextP
                    iterator.nextP.prev = n
                    n.prev = iterator
                    iterator.nextP = n

                else:
                    iterator = iterator.nextP

        return None


def main():
    l = DLL()
    l.insertNode(10)
    l.insertNode(1)
    l.insertNode(25)
    l.insertNode(12)

    l.findNode(9)
    l.findNode(12)
    l.insertNode(111)
    print(l.size)


if __name__ == '__main__':
    main()