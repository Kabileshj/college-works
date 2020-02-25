class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def push(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def get_prev_node(self, ref_node):
        current = self.head
        while current and current.next != ref_node:
            current = current.next
        return current

    def is_palindrome(self):
        start = self.head
        end = self.last_node
        while start != end and end.next != start:
            if start.data != end.data:
                return False
            start = start.next
            end = self.get_prev_node(end)
        return True

#Driver code
list = LinkedList()
array = input().split()
for i in array:
    list.push(i)
if list.is_palindrome():
    print('yes')
else:
    print('no')