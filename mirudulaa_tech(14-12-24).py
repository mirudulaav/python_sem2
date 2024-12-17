#1
def Merge(word1, word2):
    merge = []
    i, j = 0, 0      
    while i < len(word1) and j < len(word2):
        merge.append(word1[i]) 
        merge.append(word2[j])  
        i += 1
        j += 1
    merge.extend(word1[i:])
    merge.extend(word2[j:])
    return ''.join(merge)
word1 = input("Enter word1: ")
word2 = input("Enter word2: ")
merged = Merge(word1, word2)
print("Merged String:", merged)

#2
def can_place_flowers(flowerbed, n):
    count = 0
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i] == 0:
            empty_prev = (i == 0 or flowerbed[i-1] == 0)
            empty_next = (i == length-1 or flowerbed[i+1] == 0)
            if empty_prev and empty_next:
                flowerbed[i] = 1
                count += 1
        if count >= n:
            return True
    return False
print(can_place_flowers([1,0,0,0,1], 1))  
print(can_place_flowers([1,0,0,0,1], 2))  
