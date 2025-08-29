#question one

class Books:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def showDetails(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
    
    def read_book(self):
         print(f"I am currently reading : {self.title} by {self.author}")

class ChristainBook(Books):
    def __init__(self, title, author, price, theme):
        super().__init__(title, author, price)
        self.theme = theme

    def showDetails(self):
        super().showDetails()  
        print(f"Theme: {self.theme}")  

    def sermon(self):
         print(f"reflecting on Who I am: {self.title}")


ChristainBook = ChristainBook("The Purpose driven Life", "Rick Warren", 50, "Spiritual growth")
print("christain Book:")
ChristainBook.showDetails()
ChristainBook.read_book()
ChristainBook.sermon()
print()

#Question Two
class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move():
        print(f"{self.name} is moving")

class car(Vehicle):
    def move(self):
        print(f"{self.name} is driving")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is Flying")

        
class Ship(Vehicle):
    def move(self):
        print(f"{self.name} is Sailing")


car = car("Avalon")
plane = Plane("AirPeace")
ship = Ship("Titanic")

car.move()
plane.move()
ship.move()


