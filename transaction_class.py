
class Transaction:
    def __init__(self, amount, category, description, type):
        self.amount = amount
        self.category = category
        self.description = description
        self.type = type

    def __str__(self):
        return str(self.amount) + " " + str(self.category) + " " + str(self.description) + " " + str(self.type)










        
        