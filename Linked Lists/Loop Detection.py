class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 
	def __init__(self): 
		self.head = None

	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	def detectLoop(self): 
		s = set() 
		temp = self.head 
		while (temp): 
			if (temp in s): 
				print(temp.data)
				return True
			s.add(temp) 	
			temp = temp.next
		return False

# Driver program  
llist = LinkedList() 
for i in [int(i) for i in input().split()][::-1]:	
	llist.push(i)  
llist.head.next.next.next.next = llist.head 
if( llist.detectLoop()): 
	print ("Loop found") 
else : 
	print ("No Loop ") 