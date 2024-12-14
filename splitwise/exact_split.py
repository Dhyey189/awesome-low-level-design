class ExactSplit:
    def __init__(self, total_amount, members, payer):
        self._total_amount = total_amount
        self._members = members
        self._payer = payer

    def split_between(self, share_in_amount: dict):
        if sum(share_in_amount.values()) != self._total_amount:
            print(f"Incorrect Data! total must be {self._total_amount}.")
        else:
            for user in self._members:
                if user != self._payer and share_in_amount.get(user):
                    user.update_balances(self._payer, share_in_amount[user])
