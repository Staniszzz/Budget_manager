from transaction_class import Transaction

class Budget:
    def __init__(self):
        self.budget = 0
        self.__transaction_list = []
        self.__value_of_budget = 0

    def add_transaction(self, transaction):
        if isinstance(transaction,Transaction):
            self.__transaction_list.append(transaction)
            if transaction.type == "przychód":
                self.__value_of_budget += transaction.amount
            elif transaction.type == "wydatek":
                self.__value_of_budget -= transaction.amount
            else:
                raise ValueError("Transakcja musi być w formacie 'przychód' lub 'wydatek'")




    def __str__(self):
        str_data = "Lista wszystkich transakcji: "
        for el in self.__transaction_list:
            str_data += (("Kwota Transakcji: " + str(el.amount) + "\nKategoria: " +  el.category + "\nOpis Transakcji: " + el.description + "\nRodzaj: " + el.type + "\n" + "\n"))
        str_data += "Aktualny Bilans: " + str(self.__value_of_budget)
        return str_data
    
    


