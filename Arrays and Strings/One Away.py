#function to check the strings 
def isOneAway(string_one,string_two):
    m = len(string_one)
    n = len(string_two)
    if abs( m - n ) > 1:
        return False
    count = 0
    i = 0
    j = 0
    while i < m and j < n:
        if string_one[i] != string_two[j]:
            if count == 1:
                return False
            if m > n:
                i+=1
            elif m < n:
                j+=1
            else:
                i+=1
                j+=1
            count += 1
        else:
            i+=1
            j+=1
    if i < m and j < n:
        count += 1
    return True

#Driver code
string_one = input()
string_two = input()
if isOneAway(string_one,string_two):
    print('Yes , the given string '+string_one+' is one away from '+string_two)
else:
    print('No , the given string '+string_one+' is not one away from '+string_two)