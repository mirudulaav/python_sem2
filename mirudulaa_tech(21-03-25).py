def swap_strings(s1, s2): #Apple,Mango
    s1= s1 + s2  #s1=AppleMango,s2=Mango
    s2= s1[:len(s1) - len(s2)]  #s2= s1[:10 - 5] = s1[:5] =Apple
    s1= s1[len(s2):]  #s1= s1[5:]=Mango
    return s1, s2
word1=input("Enter first string:")
word2= input("Enter second string:")
word1, word2= swap_strings(word1, word2)
print("After swapping:")
print("String1:", word1)
print("String2:", word2)


