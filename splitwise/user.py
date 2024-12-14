from group import Group
from transaction import Transaction

class User:
    def __init__(self, name, email):
        self._id = id(self)
        self._name = name
        self._email = email
        self._balances = {}
        self._groups = []
        self._transactions = []

        print(f"User Created: id = {self._id}.")

    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name

    def update_balances(self, sender, amount):
        if self._balances.get(sender.get_id()):
            self._balances[sender.get_id()] += amount
        else:
            self._balances[sender.get_id()] = amount

        if sender._balances.get(self.get_id()):
            sender._balances[self.get_id()] -= amount
        else:
            sender._balances[self.get_id()] = -amount

        transaction = Transaction(
            sender=sender,
            receiver=self,
            amount=amount
        )
        transaction.print_transaction()

        self._transactions.append(transaction)
        sender._transactions.append(transaction)

        return transaction

    def add_group(self, title, description, members):
        group = Group(title, description, members)

        self._groups.append(group)

        return group
    
    def get_balances(self):
        return self._balances
