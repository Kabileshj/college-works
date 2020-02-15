#function for checkpermutation
def checkPermutation(string_first,string_second):
    count_one = [0] * no_of_char
    count_two = [0] * no_of_char
    for i in string_first:
        count_one[ord(i)]+=1
    for i in string_second:
        count_two[ord(i)]+=1
    if len(string_first) != len(string_second):
        return False
    for i in range(no_of_char):
        if count_one[i] != count_two[i]:
            return False
    return True

#Driver code
no_of_char = 256
string_first = input()
string_second = input()
if checkPermutation(string_first,string_second):
    print(string_first + ' is a permutation of ' + string_second)
else:
    print(string_first + ' is not a permutaion of ' + string_second)