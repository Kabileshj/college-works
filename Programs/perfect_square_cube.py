import math
def is_cube(n):
    root = n**(1./3.)
    if round(root) ** 3 == n:
        return True
    else:
        return False
def is_square(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False
x=int(input())
i=x
while i<=x:
  if is_cube(i) and is_square(i) :
    print(i)
    break
  i-=1