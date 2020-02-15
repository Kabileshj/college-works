#isUnique to check unique characters in a string
def isUnique(input):
    checker = 0
    for i in range(len(input)):
        index = (ord(input[i]) - ord('a'))
        if (checker & (1 << index)) > 0:
            return False
        checker = checker | (1 << index)
    return True
#Driver code
input = input()
if isUnique(input):
    print(input+' has unique characters')
else:
    print(input+' has duplicates')