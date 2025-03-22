def longest_palindromic_substring(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
    return longest

s1 = input("Enter string:")
print(f"Long Palindrome: {longest_palindromic_substring(s1)}")  
