from equal_split import EqualSplit
from split_method import SplitMethod
from percent_split import PercentSplit
from exact_split import ExactSplit

class Expense:
    def __init__(self, title, total_amount, members, payer):
        self._id = id(self)
        self._title = title
        self._total_amount = total_amount
        self._members = members
        self._payer = payer
        print(f"Expense Created: id = {self._id}.")

    @staticmethod
    def get_split_method_class(split_method):
        if split_method == SplitMethod.EQUAL_SPLIT:
            return EqualSplit
        elif split_method == SplitMethod.PERCENTAGE_SPLIT:
            return PercentSplit
        else:
            return ExactSplit

    def split(self, split_method = SplitMethod.EQUAL_SPLIT, split_rules = {}):
        split_method_class = self.__class__.get_split_method_class(split_method)
        smc = split_method_class(self._total_amount, self._members, self._payer)
        
        if smc.__class__ == EqualSplit:
            smc.split_between()
        else:
            smc.split_between(split_rules)
