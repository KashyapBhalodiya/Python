class Item:
    pass # placeholder for future code means when it's executed nothing happens but you avoid getting an error
item1 = Item()

class Items:
    def calculate_total_price(self, x, y):
        return x * y

item2 = Items()
a = item2.calculate_total_price(3, 2)
print(a)


## constructor
class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"My name is {name}")

c1 = MyClass("Niraj")
print(c1)





