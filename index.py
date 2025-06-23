#Object Oriented Porgramming

#Encapsulation -- storing data, method in a single class so no other class can access it
class shop():
    def __init__(self,name,email,balance):
        self.name = name
        self.email = email
        self.balance = balance

    def user_info(self):
        print(f"Name:{self.name}\nEmail:{self.email}\nWallet Balance:{self.balance}")
        print("**********")

class customer(shop):
    def buy_item(self,amount):
        if amount > self.balance:
            print("You can't buy this!")
        else:
            self.balance -= amount
            print('item purchased succesfully')
            print(f"Remaning Balance:{self.balance}")
    def role_info(self):
        print("I am customer")

class seller(shop):
    def sold_item(self,amount):
        print(f"Amount Received {amount}")
    def role_info(self):
        print("I am seller")

new_customer = customer("Raj","raj@gmail.com",1000)
new_seller = seller("rajcompany","rajcompany@gmail.com",3000)


#inheritance -- pasing properties from parent to child classes 
new_customer.user_info()
new_seller.user_info()

new_customer.buy_item(200)
new_seller.sold_item(200)

#polymorphism -- same name of method but different usage 
for i in (new_customer,new_seller):
    i.role_info()
