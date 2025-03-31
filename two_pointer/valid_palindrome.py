'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Time Complexity: O(n)
Space Complexity: O(1)
'''

def isPalindrome(s):
    # add your logic here
    i = 0
    j = len(s)-1
    while i<j:
        if not s[i].isalnum():
            i+=1
        elif not s[j].isalnum():
            j-=1
        else:
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
    return True

# Original test cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # Expected: True
print(isPalindrome("race a car"))  # Expected: False
print(isPalindrome(" "))  # Expected: True

# Additional test cases
print(isPalindrome("12321"))  # Expected: True (numeric palindrome)
print(isPalindrome("Never odd or even"))  # Expected: True
print(isPalindrome("hello world"))  # Expected: False
print(isPalindrome("Madam, I'm Adam"))  # Expected: True
print(isPalindrome("123 321"))  # Expected: True
print(isPalindrome("0P"))  # Expected: False
print(isPalindrome(".,"))  # Expected: True (empty after removing non-alphanumeric)
print(isPalindrome("Was it a car or a cat I saw?"))  # Expected: True
print(isPalindrome("12@#$%^&*()21"))  # Expected: True (after removing special characters)
print(isPalindrome("A1b2C3c2b1a"))  # Expected: True (alphanumeric mix)
