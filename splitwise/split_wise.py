from threading import Lock
from split_method import SplitMethod
from user import User

class SplitWise:
    _instance = None
    _users = []
    
    _lock = Lock()
	
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)

        return cls._instance
				
    @classmethod
    def get_instance(cls):
        return cls()
    
    def add_user(self, name, email):
        user = User(name, email)

        self._users.append(user)

        return user

    def add_group(self, user, title, description, members):
        return user.add_group(title, description, members)

    def add_expense(self, user, group, title, total_amount, participating_members, payer, split_method = SplitMethod.EQUAL_SPLIT, split_rules = {}):
        if group not in user._groups:
            print("Incorrect Data! provided group does not belongs to given user.")
            return
        
        return group.add_expense(title, total_amount, participating_members, payer, split_method = SplitMethod.EQUAL_SPLIT, split_rules = {})

    def update_balances(self, user, payer, amount):
        user.update_balances(payer, amount)

    
        