from item import Item
from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)



print(Item.check_integer(8.3))
phone1 = Phone("iphone",1000,3)
phone1.calculate_price()
print(Phone.all)
