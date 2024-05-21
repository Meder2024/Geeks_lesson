class MagicCalculator:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        return MagicCalculator(self.number_1 + other.number_1, self.number_2 + other.number_2)

    def __sub__(self, other):
        return MagicCalculator(self.number_1 - other.number_1, self.number_2 - other.number_2)
    
    def __mul__(self, other):
        return MagicCalculator(self.number_1 * other.number_1, self.number_2 * other.number_2)
    
    def __truediv__(self, other):
        return MagicCalculator(self.number_1 / other.number_1, self.number_2 / other.number_2)
    
    def __floordiv__(self, other):
        return MagicCalculator(self.number_1 // other.number_1, self.number_2 // other.number_2)
    
    def __str__(self):
        return f"({self.number_1}, {self.number_2})"


example_num_1 = MagicCalculator(100, 200)
example_num_2 = MagicCalculator(10, 20)

print(example_num_1 + example_num_2)
print(example_num_1 - example_num_2)
print(example_num_1 * example_num_2)
print(example_num_1 / example_num_2)
print(example_num_1 // example_num_2)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __str__(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"

book1 = Book("Биринчи мугалим", "Чингиз Айтматов", 1962)
book2 = Book("Белый параход", "Чингиз Айтматов", 1970)

print(book1)
print(book2)
print(book1 > book2)
print(book1 < book2)
print(book1 == book2)
print(book1 != book2)
print(book1 >= book2)
print(book1 <= book2)