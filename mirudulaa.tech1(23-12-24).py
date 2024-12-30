#2
list1= [2,3,5,6,8,1,3,5,6,6]
unique_list=[]
dup_list=[]
for num in list1:
    if num not in unique_list:
        unique_list.append(num)
    elif num in unique_list:
        dup_list.append(num)
print("List after removing duplicate elements:", unique_list)
print("Duplicate list:", dup_list)
unique_list.sort(reverse=True)
print("Descending order:",unique_list)
    
#4
l1=[1,2,3,4, 12, 30]
l2=[4,5,6,12,30]
common=[]
for num in l1:
    if num in l2:
        common.append(num)
print("Common Elements:", common)

#5
string1= "Python Programming"
count=string1.split()
length=len(count)
print("Number of words in string:", length)

#8
import re
def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Not a valid email address.")
input_email = input("Enter email: ")
valid_email(input_email)

#10
import re
def extract_hashtags(text):
    pattern= r'#\w+'
    hashtags= re.findall(pattern, text)
    return hashtags
text1=input("Enter text with characters:")
hashtags=extract_hashtags(text1)
print("Extracted hashtags:", hashtags)
    
        






























    
