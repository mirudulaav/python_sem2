character=input()
if 'A'<=character<='Z':
    c=ord(character)+32
    converted=chr(c)
print(converted)

charac = input("Enter string: ")
for i in charac:
    if 'A' <= i <= 'Z':
        c = ord(i)
        convert = chr(c + 32)
        print(convert, end=" ")
    else:
        print(i, end=" ")

def lowcase(ch):
    p=ord(ch)
    q=chr(p+32)
    print(q, end=" ")
def upcase(ch):
    m=ord(ch)
    s=chr(m-32)
    print(s, end=" ")
string1=input()
for i in string1:
    if 'A' <= i <= 'Z':
      lowcase(i)
    elif 'a'<=i<='z':
        upcase(i)
    
#in a string--> remove numbers
list1=['apPLe', 'oraNGE', 'manGO', 'waterMELON']
upper_lower=[]
for string in list1:
    upper_lower_str=" "
    for i in string:
        if 'a'<=i<='z':
            upper_lower_str+=chr(ord(i)-32)
        elif 'A'<=i<='Z':
            upper_lower_str+=chr(ord(i)+32)
    upper_lower.append(upper_lower_str)
print(f"New List: {upper_lower}")


    
    
