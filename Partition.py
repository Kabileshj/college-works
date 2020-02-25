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

    def partition(self, head, x):
        current = head
        before = Node(0)
        after = Node(0)
        before_head = before
        after_head = after
        while current:
            if current.data < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
            after.next = None
        before.next = after_head.next
        self.head = before_head.next

#Driver code
list1 = LinkedList()
part_value = int(input())
input = [int(i) for i in input().split()]
for i in input:
    list1.push(i)
list1.partition(list1.head, part_value)
list1.printlist()