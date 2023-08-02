import csv

class Item:
    all = []
    payrate = 0.8
    def __init__(self,name : str,price: float,quantity:float):
        assert price >= 0,"Price can't be negative!"
        assert quantity >= 0,"Quantity can't be negative!"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_price(self):
        print(self.price*self.quantity)

    def apply_discount(self):
        self.price = self.price * self.payrate

    @classmethod
    def instantiate_from_csv(cls):
        with open ("item.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=(item.get('name')),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
            )

    @staticmethod
    def check_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"item('{self.name}',{self.price},{self.quantity})"

# Item.instantiate_from_csv()
# print(Item.all)
print(Item.check_integer(8.3))
