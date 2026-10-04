class Book():
    def __init__(self,title,author,isbn,is_available=True):
        self.b_title=title
        self.b_author=author
        self.b_isbn=isbn
        self.available=is_available

    def display_info(self):
        print(f" book title={self.b_title} \n book autor={self.b_author} \n book isbn={self.b_isbn} \n book status={self.available}")

class Member():
   def __init__(self, member_id, name, borrowed_books=None):
    self.m_id = member_id
    self.m_name = name
    self.m_bbks = borrowed_books if borrowed_books is not None else []

    def borrow_book(self,book):
        self.m_bbks.append(book)
        return self.m_bbks
    def remove_book(self,book):
        self.m_bbks.remove(book)
        return self.m_bbks
    def display_borrowed_books(self):
        print(self.m_bbks)

class Library():
    def __init__(self, books=None, members=None):
     self.l_books = books if books is not None else []
     self.l_members = members if members is not None else []
    def add_book(self,book):
        self.l_books.append(book)
        return self.l_books
    def register_mem(self,member):
        self.l_members.append(member)
        return self.l_members
    def issue_book(self,isbn,memeber_id):
        pass
    
    