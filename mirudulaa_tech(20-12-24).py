import random
import re
class Member:
    def __init__(self, mem_id, name, email):
        self.mem_id=mem_id
        self.name=name
        self.email=email

    def generate_mem_id(self):
        Id="LIB"
        num= random.randint(1000,9999)
        self.mem_id=f"{Id}{num}"
        print(mem_id)

    def verify_mem_id(mem_id):
        if self.mem_id[0:3]=="LIB" and self.mem_id[3:].isdigit():
            print("Member ID is valid")
        else:
             print("Member ID is invalid")

    def verify_email(email):
        pattern= r'^[a-z A-Z 0-9._%+-]+@[a-z A-Z 0-9.-]+\.[a-z A-Z] {2,}$'
        if re.match(pattern, self.email):
            print("Email is Valid")
        else:
            print("Email is Invalid")

class Library(Member):
    def __init__(self, book, member):
        self.book=book
        self.member=member

    def add_book(self, book_id, title, author):
        self.books[book_id] = {'title': title, 'author': author}
        print(f"Book '{title}' by {author} added to the library.")

    def register_member(self, name, email):
        mem1 = Member(name, email)
        self.member.append(mem1)
        print(f"Member '{name}' registered with ID {mem1.mem_id}.")

    def borrow_book(self, mem_id, book_id):
        for mem in self.member:
            if  member[mem_id]=="mem_id":
                print(f"Book '{self.books[book_id]['title']}' borrowed by member with ID {member_id}.")
            else:
                print("Invalid member ID or book ID.")

    def return_book(self, member_id, book_id):
        for member in self.members:
            if member['member_id'] == member_id and book_id in self.books:
                print(f"Book '{self.books[book_id]['title']}' returned by member with ID {member_id}.")
            else:
                print("Invalid member ID or book ID.")
                
library = Library()
library.register_member('Alice', 'alice@example.com')
library.add_book('B001', '1984', 'George Orwell')
library.borrow_book('LIB1001', 'B001')
library.return_book('LIB1001', 'B001')
    
        
            
