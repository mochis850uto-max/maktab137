class Library:
    def __init__(self, books: list):
        self.books = books
    
    def __len__(self):
        return len(self.books)
    
    def __add__(self , new_library):
        if isinstance(new_library, Library):
            new_list = self.books + new_library.books
            return new_list
        
    def __str__(self):
        return str(self.books)
    
    def __del__(self):
        print(f"library was deleted")

l1 = Library(["1984", "my war", "animal farm"])
print(l1)
l2 = Library(["c+", "python", "java"])
print(len(l1))
print(len(l2))
l3 = l1 + l2
print(l3)
print(l2)