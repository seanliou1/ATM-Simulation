# implement all custom exceptions here
class InvalidAccount(Exception):
    """For Transfer transactions, if the account numbers for
both sender and receiver are the same raise invalid account exception."""
    def __init__(self, message = "You have selected an invalid account."):
        self.message = message
        super().__init__(self.message)

class AccountNotFound(Exception):
    """Accepts an account number and checks if the account exists.
Raise account not found exception"""
    def __init__(self, message = "Account not found."):
        self.message = message
        super().__init__(self.message)

class InsufficientFunds(Exception):
    """Raise exception if debit amount is greater than the account balance."""
    def __init__(self, message = "Insufficient funds."):
        self.message = message
        super().__init__(self.message)

class InvalidATMCard(Exception):
    """Raise exception if ATM card user input is invalid"""
    def __init__(self, message = "You have inserted an invalid card.\nYour card has been returned."):
        self.message = message
        super().__init__(self.message)

class InvalidPinNumber(Exception):
    """Raise exception if pin number input does not match customer pin"""
    def __init__(self, message = "You have entered an invalid pin.\nYour card has been returned."):
        self.message = message
        super().__init__(self.message)