#function to check permutation of a palindrome
def palindrome_permutation(string):
    count = [0] * no_of_char
    for i in range(len(string)):
        count[ord(string[i])] = count[ord(string[i])] + 1
    single = 0
    for i in range(no_of_char):
        if count[i] & 1 :
            single = single + 1
        if single > 1 :
            return False
    return True
#Driver code
no_of_char = 256
string = input()
if palindrome_permutation(string):
    print(string + ' is a permutation of a palindrome')
else:
    print(string + ' is not a permutation of a palindrome')