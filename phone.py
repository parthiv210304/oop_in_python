from item import Item
class Phone(Item):
    def __init__(self,name:str,price:int,quantity:int):
        super().__init__(name,price,quantity)