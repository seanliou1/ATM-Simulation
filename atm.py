# import any necessary libraries/scripts here
from atm_transaction import Withdrawal, Transfer
from additional_exceptions import InvalidAccount, InvalidATMCard

class ATM:
    def __init__(self, loc: str, managed_by: object) -> None:
        self.address = loc
        self.bank = managed_by
        self.__current_card = None

    def get_current_card(self) -> object:
        """Getter for the current ATM card"""
        return self.__current_card

    def set_current_card(self, card: object) -> None:
        """Setter for the current ATM card"""
        self.__current_card = card

    def transactions(self, trans_type: str, amt: str, acct_type: str,
                     trans_acct_num: object = None) -> None:
        """Process the transaction according to the transaction type. Return the status
of the transaction or raise an exception if the transaction fail"""
        if trans_type == "withdrawal":
            #get the account
            target_account = self.get_current_card().access(acct_type)
            #initialize the Withdrawal object
            wdl_txn = Withdrawal(amt)
            wdl_txn.withdraw(target_account)
        elif trans_type == "transfer":
            target_account = self.get_current_card().access(acct_type)
            if target_account == trans_acct_num:
                raise InvalidAccount
            else:
                target_account = self.get_current_card().access(acct_type)
                tfr_txn = Transfer(amt)
                tfr_txn.update(target_account, amt, trans_acct_num)

    def check_accts(self) -> bool:
        """Check if user has 1 or 2 accounts. Returns True if there is 2
otherwise return False"""
        if len(self.get_current_card().get_owned_by().get_acct_list()) == 2:
            return True
        return False

    def check_pin(self, pin:str) -> bool:
        """Accepts the user input pin and check with the bank if it is valid"""
        self.bank.authorize_pin(self.get_current_card().get_owned_by(), pin)

    def check_card(self, card_num: str) -> bool:
        """Accept an ATM card number and checks with the bank if it is a valid card.
If it is valid, set current card attribute to this ATM card object and return True.
If it is invalid, raise an invalid card exception"""
        for card in self.bank.atm_cards:
            if card.get_card_num() == card_num:
                self.set_current_card(card)
                return True
        raise InvalidATMCard


    def show_balance(self, acct_type: str) -> str:
        """Accepts account type and returns a string message detailing
the current balance of the requested account of that customer"""
        target_account = self.get_current_card().access(acct_type)
        return f"Your {acct_type} account balance is: ${target_account.check_balance():.2f}\n"
