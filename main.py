from transaction_class import Transaction
from budget_class import Budget

### TU DODAJEMY TRANSAKCJE ###
t1 = Transaction(500,"Jedzenie","Okazjonalny","wydatek")

# KONSTRUKTOR + WYWOŁANIE FUNKCJI DODAWANIA TRANSAKCJI
budget = Budget()
budget.add_transaction(t1)


# WYŚWIETLENIE LISTY 
print(budget)