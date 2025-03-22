def palindromePairs(words):
    word_map = {word[::-1]: i for i, word in enumerate(words)}
    result = []    
    for i, word in enumerate(words):
        if word in word_map and word_map[word] != i:
            result.append([i, word_map[word]])        
        for j in range(len(word)):
            prefix, suffix = word[:j], word[j:]           
            if prefix == prefix[::-1] and suffix in word_map:
                result.append([word_map[suffix], i])           
            if suffix == suffix[::-1] and prefix in word_map:
                result.append([i, word_map[prefix]])    
    return result

words1 = ["abcd", "dcba", "lls", "s", "sssll"]
words2 = ["bat", "tab", "cat"]
print(palindromePairs(words1))  
print(palindromePairs(words2))  
