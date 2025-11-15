class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    def item_total(self):
        return self.product.price * self.quantity
p1 = Product("Laptop", 80000)
p2 = Product("Mouse", 1500)
p3 = Product("Keyboard", 3000)
c1 = CartItem(p1, 1)   
c2 = CartItem(p2, 2)  
c3 = CartItem(p3, 1)   
total_bill = c1.item_total() + c2.item_total() + c3.item_total()
print("Total Bill =", total_bill)
