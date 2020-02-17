#function to check two strings
def isSubstring(string_first,string_second):
    if len(string_first) != len(string_second):
        return False
    else:
        for i in range(len(string_first)):
            string = ''
            string += string_first[i::]
            string += string_first[:i:]
            if string == string_second:
                return True

#Driver code
string_first = input()
string_second = input()
if isSubstring(string_first,string_second):
    print(string_first + ' is a rotation of ' + string_second)
else:
    print(string_first + ' is not a rotation of ' + string_second)