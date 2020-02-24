def sortedInsert(s , element): 
	if len(s) == 0 or element > s[-1]: 
		s.append(element) 
		return
	else: 
		temp = s.pop() 
		sortedInsert(s, element) 
		s.append(temp) 

def sortStack(s): 
	if len(s) != 0: 
		temp = s.pop() 
		sortStack(s) 
		sortedInsert(s , temp) 

def printStack(s): 
	for i in s[::-1]: 
			print(i , end=" ") 
	print() 
	
# Driver Code 
if __name__=='__main__': 
	s = [ ] 
	for i in [int(i) for i in input().split()]:
		s.append(i)
	sortStack(s) 
	print("\nStack elements after sorting: ") 
	printStack(s) 