
class Transaction:
    def __init__(self, sender, receiver, amount):
        self._id = id(self)
        self._sender = sender
        self._receiver = receiver
        self._amount = amount

    def print_transaction(self):
        print(f"User({self._sender.get_name()} - {self._sender.get_id()}) sent ${self._amount} to User({self._receiver.get_name()} - {self._receiver.get_id()})")