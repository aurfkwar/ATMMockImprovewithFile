class Category:
    registry = list()

    def __init__(self, category, amount):
        self.category = category
        self.registry = list()
        self.amount = amount

    def deposit(self, amount, des = ""):
       self.registry.append({"amount" : amount, "description": des})
       self.amount += amount
       return "You have successfully deposited {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    def withdrawal(self, amount, des = ""):
        if self.check_balance(amount):
            self.registry.append({"amount" : -amount, "description": des})
            self.amount -= amount
            return "This is your withdrawal amount {} in {} category".format(amount, self.category)
        else:
            return False

    def check_balance(self, amount):
        if amount > self.amount:
            return False
        else:
            return True
        # this should return a boolean, it checks if amount is less or greater than self.amount
      

    def transfer(self, amount, category):
        if self.check_balance(amount):
            des = 'Transfer to ' + self.category
            self.withdrawal(amount, des)
            des = 'Transfer from ' + self.amount
            category.deposit(amount, des)
            return True
        else:
            return False
        # transfer between two instantiated categories
       

food_category = Category("Food", 1000)
clothing_category = Category("Clothing", 750)
car_category = Category("Car Expenses", 300)

print(food_category.deposit(250))
print(food_category.budget_balance())
print(food_category.withdrawal(200))
