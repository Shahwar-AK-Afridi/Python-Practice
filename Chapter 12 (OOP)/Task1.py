""" 
    1)Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)
    2)Add a method called move that will take two parameters, call them dx and dy. The method will cause the point to move in the x and y direction the number of units given. (Hint: you will change the values of the state of the point)
    3)Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.
    4)Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the format: "A basket of [quantity goes here] [color goes here] apples." e.g. "A basket of 4 red apples." or "A basket of 50 blue apples." (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)
    5)Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount, you see "Your account, [name goes here], has [start_amt goes here] dollars." Create an instance of this class with "Bob" as the name and 100 as the amount. Save this to the variable t1
    6)Person and Student classes using inheritance
    7)Books, PaperBooks, Ebooks and Library (Composition)
"""

#1
print("(1)Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)")

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return str(self.x)+","+str(self.y)
    
    def reflect_x(self):
        self.y = (-1)*self.y
        return Point(self.x,self.y)

p1 = Point(3,5)
print(p1)
print(p1.reflect_x())
p5 = p1.reflect_x()
print(p5)

print("----------------------------------------------------------")


#2
print("(2)Add a method called move that will take two parameters, call them dx and dy. The method will cause the point to move in the x and y direction the number of units given. (Hint: you will change the values of the state of the point)")

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # Put your new method here
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    def __str__(self):
        return str(self.x)+","+str(self.y)


p1 = Point(3,5)
print(p1)
p1.move(10,20)
print(p1)
print(p1.x)

print("----------------------------------------------------------")

#3
print("(3)Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.")

class Bike:
    
    def __init__(self, c, p):
        self.color = c
        self.price = p
        

testOne = Bike("blue",89.99)
testTwo = Bike("purple",25.0)

print("----------------------------------------------------------")

#4
print("(4)Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. The constructor should initialize two instance variables: apple_color and apple_quantity. Write a class method called increase that increases the quantity by 1 each time it is invoked. You should also write a __str__ method for this class that returns a string of the format: A basket of [quantity goes here] [color goes here] apples. e.g. A basket of 4 red apples. or A basket of 50 blue apples. (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)")

class AppleBasket():
    
    def __init__(self, color, quantity):
        self.apple_color = color
        self.apple_quantity = quantity
        
    def increase(self):
        self.apple_quantity += 1
        
    def __str__(self):
        representation = "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)
        return representation
    
apple1 = AppleBasket("GOLDEN", 12)
print(apple1)
apple2 = AppleBasket("red", 4)
print(apple2)

print("----------------------------------------------------------")

#5
print("(5)Define a class called BankAccount that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: name and amt. Add a string method so that when you print an instance of BankAccount, you see ,Your account, [name goes here], has [start_amt goes here] dollars., Create an instance of this class with ""Bob"" as the name and 100 as the amount. Save this to the variable t1")

class BankAccount:
    
    def __init__(self, name, money):
        self.name = name
        self.amt = money
        
    def __str__(self):
        representation = "Your account, {}, has {} dollars.".format(self.name, self.amt)
        return representation
    
t1 = BankAccount("Bob", 100)
print(t1)
        
print("----------------------------------------------------------")

#6
print("(6)Person and Student classes using inheritance")

current_year = 2019

class Person():

    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born

    def getAge(self):
        age = current_year - self.year_born
        return age
    
    def __str__(self):
        representation = "Name:{} Age:{}".format(self.name, self.getAge())
        return representation
        
shahwar = Person("shahwar",1999)
print(shahwar)

class student(Person):

    def __init__(self, name, year_born):
        super().__init__(name, year_born)
        self.knowledge = 0

    def study(self):
        self.knowledge += 1

    def __str__(self):
        representation = super().__str__() + "Knowledge:{}".format(self.knowledge)
        return representation

afridi = student("aka",1999)
print(afridi)
afridi.study()
print(afridi)
afridi.study()
print(afridi)

print("----------------------------------------------------------")

#7
print("(7)Books, PaperBooks, Ebooks and Library (Composition)")

class Books():

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        representation = "{} by {}".format(self.title, self.author)
        return representation
    
class PaperBook(Books):

    def __init__(self, title, author, num_pages):
        super().__init__(title, author)
        self.num_pages = num_pages

    def __str__(self):
        representation = "Paper Book=>" + super().__str__()
        return representation
    
class Ebook(Books):

    def __init__(self, title, author, size):
        super().__init__(title, author)
        self.size = size

    def __str__(self):
        representation = "Ebook=>" + super().__str__()
        return representation


class library():
    """This Library class is composed of list of books this is called composition"""
    def __init__(self) -> None:
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def getNumBooks(self):
        num_of_books = len(self.books)
        return num_of_books
    
    def lstofbooks(self):
        return self.books
    
paper = PaperBook("Python For Everybody", "Charles", 1000)
print(paper)
ebook = Ebook("Automation Using Python", "Charles", 500)
print(ebook)

lib = library()
lib.addBook(paper)
lib.addBook(ebook)

#only printing title of book/objects
for book in lib.lstofbooks():
    print(book.title)

#only printing author of books/objects
for book in lib.lstofbooks():
    print(book.author)

print("----------------------------------------------------------")
