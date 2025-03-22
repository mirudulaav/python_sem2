def find_longest_vowel_substring(s):
    vowels = set("aeiou")
    max_length = 0
    result = " "
    for i in range(len(s)):
        seen = set()
        substring = " "
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            substring += s[j]
            if any(char in vowels for char in substring):
                if len(substring) > max_length or (len(substring) == max_length and substring < result):
                    max_length = len(substring)
                    result = substring
    return max_length, result
print(find_longest_vowel_substring("aeioxyz"))
print(find_longest_vowel_substring("bcdfghjklmnp"))
