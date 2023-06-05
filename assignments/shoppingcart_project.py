"""
We want to build an online shopping cart system that allows users to add products to their cart, calculate the total cost, apply discounts, and generate an invoice. The system should include the following functionalities.
--> Adding products to the cart
--> Removing products from the cart
--> Calculation the total cost
--> Applying discounts based on user type
--> Generating an invoice
"""

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return(f"Item: {self.name}  Price: {self.price}")
          
class Users:
    def __init__(self,user_name,num_of_products):
        self.name = user_name
        self.products = num_of_products
        self.is_premium = False
        self.is_admin()
        self.cart_creation()

    def is_admin(self):
        bool_value = input(f"Do you want to set {self.name} as a premium user ? \n Enter y or n: ")
        if (bool_value == 'y' or bool_value == 'Y'):
            self.is_premium = True

    def cart_creation(self):
        cart = ShoppingCart()

        #defining different products
        product1 = Product("Shirt",20)
        product2 = Product("Pants",30)
        product3 = Product("Shoes",50)

        #display items on the store
        print(f"Items available on the store. \n")
        print("--------------------------------- \n")
        print(product1)
        print(product2)
        print(product3)
        print("\n ------------------------------- \n")

        #add products to the cart
        if(self.products == 3):
            cart.add_products(product1)
            cart.add_products(product2)
            cart.add_products(product3)
        elif(self.products == 2):
            cart.add_products(product1)
            cart.add_products(product2)
        else:
            cart.add_products(product1)

        print(f"{self.name} has {self.products} item in the cart. \n")
        #generate and print the invoice
        invoice = cart.generate_invoice(self)
        print(invoice)


def discount_10_percent(func):
    def wrapper(cost):
        total_price = func(cost)
        price_with_discount = total_price * 0.9
        return price_with_discount
    return wrapper

class ShoppingCart:
    def __init__(self):
        self.products = []
    
    def add_products(self,product):
        self.products.append(product)
        
    def remove_product(self,product):
        self. products.remove(product)
        
    def calculate_total_cost(self):
        total_cost = sum(product.price for product in self.products)
        return total_cost
    
    @discount_10_percent
    def calculate_discounted_cost(self):
        total_cost = sum(product.price for product in self.products)
        return total_cost
    
    def generate_invoice(self,user):
        invoice = f"Invoice for {user.name}:\n"
        invoice += "======================== \n"
        for product in self.products:
            invoice += f"{product.name}: ${product.price}\n"
        total_cost = self.calculate_total_cost()
        if user.is_premium:
            invoice += "---------------------\n"
            invoice += f"Sub-total: ${total_cost}\n"
            final_cost = self.calculate_discounted_cost()
            invoice += f"Discount (10%): ${total_cost - final_cost}\n"
            total_cost = final_cost
        invoice += "------------------------\n"
        invoice += f"Total cost: ${total_cost}"
        return invoice
    
    def get_products(self):
        yield from self.products

class ShoppingCart:
    def __init__(self):
        self.products = []
    
    def add_products(self,product):
        self.products.append(product)
        
    def remove_product(self,product):
        self. products.remove(product)
        
    def calculate_total_cost(self):
        total_cost = sum(product.price for product in self.products)
        return total_cost
    
    @discount_10_percent
    def calculate_discounted_cost(self):
        total_cost = sum(product.price for product in self.products)
        return total_cost
    
    def generate_invoice(self,user):
        invoice = f"Invoice for {user.name}:\n"
        invoice += "======================== \n"
        for product in self.products:
            invoice += f"{product.name}: ${product.price}\n"
        total_cost = self.calculate_total_cost()
        if user.is_premium:
            invoice += "---------------------\n"
            invoice += f"Sub-total: ${total_cost}\n"
            final_cost = self.calculate_discounted_cost()
            invoice += f"Discount (10%): ${total_cost - final_cost}\n"
            total_cost = final_cost
        invoice += "------------------------\n"
        invoice += f"Total cost: ${total_cost}"
        return invoice
    
    def get_products(self):
        yield from self.products



# create a user with username and number of products in their cart
user1 = Users("Rita", 3)
user2 = Users("John", 2)

