from expense import Expense
from split_method import SplitMethod

class Group:

    def __init__(self, title, description = None, members = []):
        self._id = id(self)
        self._title = title
        self._description = description
        self._members = members
        self._expenses = []

        print(f"Group Created: id = {self._id}.")

    def add_expense(self, title, total_amount, participating_members, payer, split_method = SplitMethod.EQUAL_SPLIT, split_rules = {}):
        for user in participating_members:
            if user not in self._members:
                print(f"Incorrect Data! user: {id(user)} does not belongs to this group.")
                return

        expense = Expense(title, total_amount, participating_members, payer)
        expense.split(split_method, split_rules)
        
        self._expenses.append(expense)

        return expense

    