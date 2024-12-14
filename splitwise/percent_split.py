class PercentSplit:
    def __init__(self, total_amount, members, payer):
        self._total_amount = total_amount
        self._members = members
        self._payer = payer

    def split_between(self, share_in_percent: dict):
        if sum(share_in_percent.values()) != 100:
            print("Incorrect Data! Percentage total must be 100.")
        else:
            for user in self._members:
                if user != self._payer and share_in_percent.get(user):
                    user.update_balances(self._payer, share_in_percent[user] * self._total_amount / 100)
        
        
