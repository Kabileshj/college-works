class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def printlist(self):
        current = self.head
        while current:
            if current.next:
                print(current.data, end="->")
            else:
                print(current.data)
            current = current.next

    def intersection(self, first, second):
        dictionary = {}
        while first:
            dictionary[first.data] = first.next
            first = first.next
        while second:
            if second.data in dictionary.keys():
                return second.data
            second = second.next
        return None

#Driver code
list1 = LinkedList()
list2 = LinkedList()
array = [int(i) for i in input().split()]
for i in array:
    list1.push(i)
array1 = [int(i) for i in input().split()]
for i in array1:
    list2.push(i)
list3 = LinkedList()
print(list3.intersection(list1.head, list2.head))