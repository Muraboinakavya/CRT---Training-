class Product:
     def __init__(self,product_name,price):
         self.__product_name = product_name
         self.__price = price
     def get_product_name(self):
         return self.__product_name
     def get_price(self):
         return self.__price 
class InventoryManger(Product):
     def __init__(self,product_name,price):
         super().__init__(product_name,price)
     def get_min_price(self):
         return min(self.get_price())
     def get_max_price(self):
         return max(self.get_price())
     def count_expensive_prices(self):
         count = 0
         price = self.get_price()
         for i in range(len(price)):
            if(price[i] >=1000):
                count +=1
         return(count)
     def uppercase_name(self):
         return self.get_product_name().upper()
     def is_palindrome(self):
         product = self.get_product_name()
         reverse = product[::-1]
         if product == reverse :
          return True
         else:
            return False
product_name = input()
letter_name = input()
price = list(map(int,input().split()))
p1 = InventoryManger(product_name,price)
print(f"Product : {p1.get_product_name()}")
print(f"UpperCase :{p1.uppercase_name()}")
print(f"Minimum Price : {p1.get_min_price()}")
print(f" Expensive Count: {p1.count_expensive_prices()}")
print(f"Palindrom : {p1.is_palindrome()}")
         



