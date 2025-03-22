def longestCommonPrefix(s):
    if not s:
        return ""
    prefix = s[0] #initializing "flower" as prefix|prefix=flow|
    for word in s[1:]: #comparing next word with prefix
        while not word.startswith(prefix): #compares if "flow" startswith "flower"|compares if "flight" startswith "flow"
            prefix = prefix[:-1] #flower=flowe|flowe=flow|#flow=flo|flo=fl
            if not prefix:
                return ""
    return prefix #flow|fl

strs= ("flower","flow","flight") 
result = longestCommonPrefix(strs)
print("Longest common prefix:", result)
