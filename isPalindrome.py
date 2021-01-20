def isPalindrome():
    s = input("Give me a word, preferred to be a palindrome.")
    # if the length of s is less than 2 then it is always a palindrome.
    if len(s) < 2:
            return True

    letters = "1234567890abcdefghijklmnopqrstuvwxyz"

    newString = ""
    for char in s.lower():
        if char in letters:
            newString += char
    # compares the right side to the left side each time coming closer to the middle if they are not equal at one point then it is not a palindrome.
    leftIndex = 0
    rightIndex = len(newString) - 1

    while leftIndex < rightIndex:
        if newString[leftIndex] != newString[rightIndex]:
            return False
        leftIndex += 1
        rightIndex -= 1

    return True

class Solution:
    isPalindrome()