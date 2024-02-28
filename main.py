'''
Create a library class
display book
Brower book -(who own the book if not present)
Add book
return book

create a main functio and run an infinite while loop asking uaer for their input '''


class Library:
    def __init__(self,book_list,name):
        self.book_list=book_list
        self.name=name
        self.Browerdict={}
    
    def displaybook(self):
        print(f"we have following book in library: {self.name}")
        for book in self.book_list:
            print(book)
    def Browerbook(self,user,book):
        if book not in self.Browerdict.keys():
            self.Browerdict.update({book:user})
            print("You can Borrow Book ,Database has been updated")
        else:
            print(f"Book is already being used by {self.Browerdict[book]}")
    def addbook(self,book):
        self.book_list.append(book)
        print("Book has been added to the book list")

    def returnbook(self,book):
        self.book_list.remove(book)
if __name__ == "__main__":
    lib=Library(["Python","Think and Grow Rich","C++","Java","SQL",".Net"],"RCOEM Library")

    while(True):
        print("Welcome to the {lib.name} Library.Enter your choice to continue")
        print("1. Display a Book")
        print("2. Borrow a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice=int(input())

        if user_choice==1:
            lib.displaybook()
        elif user_choice==2:
            book=input("Enter the name of the book you want to borrow: ")
            user=input("Enter your name")
            lib.Browerbook(user,book)

        elif user_choice==3:
             book=input("Enter the name of the book you want to add: ")
             lib.addbook(book)

        
        elif user_choice==4:
             book=input("Enter the name of the book you want to return: ")
             lib.returnbook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to contiue")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2=input()
            if user_choice2=="q":
                exit()
            elif user_choice2=="c":
                continue




    