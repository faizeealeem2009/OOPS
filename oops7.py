class Products:
    def __init__(self,pid):
        self.pid=pid

class Category(Products):
    def __init__(self,pid,pcategory,pname,price):
        super().__init__(pid)
        self.pcategory=pcategory
        self.pname=pname
        self.price=price

class Order(Category):
    def __init__(self,pid,pcategory,pname,price,qty,payment_method):
        super().__init__(pid,pcategory,pname,price)
        self.qty=qty
        self.payment_method=payment_method

    def amount(self):
        print(self.pid,self.pcategory,self.pname,self.price,self.qty,self.payment_method,sep="  ")
        return self.qty*self.price

O1=Order(1021,"Electronics","Earbuds",500,6,"COD")
O2=Order(1022,"Home Appliance","Mixer",2000,4,"UPI")
O3=Order(1023,"Computers","Laptop",90000,9,"Credit")

orders=[O1,O2,O3]
total_amount=0
print("Total Bill Amount")
for o in orders:
    total_amount+=o.amount()
print("Total Bill Amount= ",total_amount)