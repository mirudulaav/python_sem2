import re
word= "Simple regular expression example"
result= re.findall("mple", word)
print(result)

space= re.search("\s", word)
print("\n The first space is at:", space.start())
