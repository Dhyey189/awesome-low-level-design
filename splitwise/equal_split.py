class EqualSplit:
    def __init__(self, total_amount, members, payer):
        self._total_amount = total_amount
        self._members = members
        self._payer = payer

    def split_between(self):
        splitted_amount = self._total_amount / len(self._members)

        for user in self._members:
            if user.get_id() != self._payer.get_id():
                user.update_balances(self._payer, splitted_amount)
