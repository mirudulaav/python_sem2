#reverse a str w/o in built function
def reverse_string(s):
    length=0
    reverse=""
    for i in s:
        length+=1
    print("Length of the word:", length)
    for i in range(length-1,-1,-1):#(5,-1,-1)
        reverse+=s[i] 
    return reverse
word=input("Enter a string:").strip()
rev= reverse_string(word)
print("Reversed string:", rev)

#Replace letter in a given string
input_string=input("Enter the string:").strip()
to_replace= input("Enter char to be replaced:")
replace_with= input("Enter char to be replaced:")
replaced_string=""
for c in input_string:
    if c==to_replace:
        replaced_string+=replace_with
    else:
        replaced_string+=c
print("Replaced string:", replaced_string)
        
        
