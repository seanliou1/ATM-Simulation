# import any necessary libraries/scripts here
from additional_exceptions import InsufficientFunds

class Account:
    def __init__(self, acct_type: str, owner_obj: object) -> None:
        self._account_type = acct_type
        self.__owner = owner_obj
        self.__balance = 0

    def check_balance(self) -> float:
        """Returns the current balance of the account."""
        return self.__balance

    def set_balance(self, bal: int | float) -> None:
        """Setter for the account balance."""
        self.__balance = bal

    def get_owner(self) -> object:
        """Getter for the owner of the account."""
        return self.__owner

    def get_acct_type(self) -> str:
        """Getter for the account type."""
        return self._account_type

    def debit(self, debit_amt:str) -> bool:
        """Debits the account by the specified amount if sufficient funds are available.
        Returns True if the debit is successful, otherwise raise an InsufficientFunds
        exception."""
        self.__validate_amount(debit_amt)

        if float(debit_amt) <= self.check_balance():
            new_balance = self.check_balance() - float(debit_amt)
            self.set_balance(new_balance)
            return True
        raise InsufficientFunds

    def credit(self, credit_amt: str) -> bool:
        """Credits the account by the specified amount."""
        self.__validate_amount(credit_amt)
        new_balance = self.check_balance() + float(credit_amt)
        self.set_balance(new_balance)
        return True

    def __validate_amount(self, amt: int | float | str) -> bool:
        """Validates that the amount is a positive number
        and does not have more than 2 decimal places."""
        s = str(amt)
        if '.' in s:
            decimal_part = s.split('.')[-1]
            if len(decimal_part) > 2:
                raise ValueError("Amount cannot have more than 2 decimal places.")
        if float(amt) < 0:
            raise ValueError("Amount cannot be negative.")
        return True

class Savings_Account(Account):
    def __init__(self, acct_no: str, owner_obj: object) -> None:
        super().__init__("savings", owner_obj)
        self.__acct_no = acct_no

    def get_acct_num(self) -> str:
        """Getter for the account number."""
        return self.__acct_no


class Current_Account(Account):
    def __init__(self, acct_no: str, owner_obj: object) -> None:
        super().__init__("current", owner_obj)
        self.__acct_no = acct_no

    def get_acct_num(self) -> str:
        """Getter for the account number."""
        return self.__acct_no
