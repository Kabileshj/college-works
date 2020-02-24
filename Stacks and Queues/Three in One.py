class KStacks: 	
	def __init__(self, k, n): 
		self.k = k 
		self.n = n
		self.arr = [0] * self.n 
		self.top = [-1] * self.k 
		self.free = 0
		self.next = [i + 1 for i in range(self.n)] 
		self.next[self.n - 1] = -1

	def isEmpty(self, sn): 
		return self.top[sn] == -1

	def isFull(self): 
		return self.free == -1

	def push(self, item, sn): 
		if self.isFull(): 
			print("Stack Overflow") 
			return
		insert_at = self.free 
		self.free = self.next[self.free] 
		self.arr[insert_at] = item 
		self.next[insert_at] = self.top[sn] 
		self.top[sn] = insert_at 

	def pop(self, sn): 
		if self.isEmpty(sn): 
			return None
		top_of_stack = self.top[sn] 
		self.top[sn] = self.next[self.top[sn]] 
		self.next[top_of_stack] = self.free 
		self.free = top_of_stack 
		return self.arr[top_of_stack] 

	def printstack(self, sn): 
		top_index = self.top[sn] 
		while (top_index != -1): 
			print(self.arr[top_index]) 
			top_index = self.next[top_index] 

# Driver Code 
print('Enter no. of parts and size : ')
n,m=map(int,input().split())
kstacks = KStacks(n,m) 
print('Enter no. of inputs to push : ')
o=int(input())
print('Enter element and part')
for i in range(o):
	k,l=map(int,input().split())
	kstacks.push(k,l) 
for i in range(n):
	print("Popped element from stack "+str(i)+" is " +str(kstacks.pop(i))) 
for i in range(n):
	kstacks.printstack(i) 