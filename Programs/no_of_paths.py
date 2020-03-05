def numberOfPaths(m, n) : 
  path=1
  for i in range(n, (m + n - 1)): 
    path*= i 
    path //= (i - n + 1) 	
  return path%100000000; 
n,m=[int(i) for i in input().split()]
print(numberOfPaths(n,m)) 
