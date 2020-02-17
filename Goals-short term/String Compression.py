#function for string compression
def sting_compression(string,n):
    op = ''
    a = ''
    for i in range(n):
        count = 1
        while i < n-1 and string[i] == string[i+1]:
            count+=1
            i+=1
        if a!= string[i]:
            op += string[i]
            op += str(count) 
            a = string[i]
    return op
#Driver code
string = input()
n = len(string)
output = sting_compression(string,n)
print(output if len(output) < n else string)