class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.final_price = price

    def display_details(self):
        print("Book Title :",self.title)
        print("Author:",self.author)
        print("Price:",self.price)

    def apply_discount(self, discount):
        discount_amount = self.price * discount / 100
        self.final_price = self.price - discount_amount

    def display_final_price(self):
        print("Final Price :", self.final_price)


book1 = Book("Python Programming","Musaddiq",500)
book1.display_details()

book1.apply_discount(10)

book1.display_final_price()