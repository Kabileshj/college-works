#function for string compression
def sting_compression(string,n):
    ans = []
    for i in range(n):
        count = 1
        while i < n-1 and string[i] == string[i+1]:
            count+=1
            i+=1
        ans.append(string[i])
        ans.append(str(count))
    op = ''.join(ans)
    return op
#Driver code
string = 'kababababesh'
n = len(string)
output = sting_compression(string,n)
print(output if len(output) < n else string)