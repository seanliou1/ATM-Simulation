# import any necessary libraries/scripts here
from datetime import datetime
from abc import ABC, abstractmethod

class ATM_Transaction(ABC):
    # implement this class according to the PDF instructions
    txn_id = 0

    def __init__(self, Date: datetime, Transaction_type: str, Amount: float) -> None:
         self.Datetime = Date
         self._txn_type = Transaction_type
         self._amount = Amount
         self.txn_id += 1

    @abstractmethod
    def update(self, cust_acc: object, amt: int, transfer_acc: int = None) -> bool:
        """Updates the account object with the transaction details.
        Returns True if the update is successful, otherwise returns False."""
        return True

class Withdrawal(ATM_Transaction):
    def __init__(self, amt: str) -> None:
        super().__init__(datetime.now(), "withdrawal", amt)

    def withdraw(self, acct_obj: object) -> bool:
        """Accepts an account object and calls update function.
        Returns the state of the update function"""
        self.update(acct_obj, self._amount)

    def update(self, acct_obj: object, amt: str, trans_acct: object = None) -> bool:
        """Updates the customer's account object with the funds to be withdrawn"""
        if acct_obj.debit(amt):
            super().update(acct_obj, amt, trans_acct)
            return True
        return False


class Transfer(ATM_Transaction):
    def __init__(self, amt: str) -> None:
        super().__init__(datetime.now(), "transfer", amt)

    def update(self, acct_obj: object, amt: str, trans_acct: object) -> bool:
        """Updates the customer's account object with funds for the transfer process
        Debit from the account being transfer from and
        credit the account being transferred to"""
        if acct_obj.debit(amt) and trans_acct.credit(amt):
            super().update(acct_obj, amt, trans_acct)
            return True
        return False
