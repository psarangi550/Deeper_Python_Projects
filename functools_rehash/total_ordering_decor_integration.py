from functools import total_ordering

@total_ordering
class Book(object):#definign the book class
    def __init__(self,name,author,page):
        self.name = name
        self.author = author
        self.page = page
    
    def _is_valid_operand(self, other):
        return (hasattr(other, "page") and hasattr(other, "page"))
    
    def __str__(self):
        return "<Book %s and Author %s> " % (self.name, self.author)
    
    def print_book(self):
        print(f" Book Name :- {self.name} --> Book Author :- {self.author} --> Book Page :-{self.page} ")
    
    def __eq__(self,other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return self.page == other.page
    
    def __lt__(self,other):
        if self._is_valid_operand(other):
            return self.page < other.page
        else:
            return NotImplemented
        

book1=Book("Python", "Corey Schafer", 100)
book2=Book("Flask", "Anthony Herbert",110)

print(book1>=book2)

    
     