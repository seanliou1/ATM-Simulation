# import any necessary libraries/scripts here
import random
from additional_exceptions import InvalidPinNumber, AccountNotFound

class Bank:
    def __init__(self, code: str, addr: str) -> None:
        self.__bank_code = code
        self.__address = addr
        self.atms = []
        self.customers = []
        self.atm_cards = []
        
    def add_customer(self, customer_obj: object, pin: str) -> None:
        """Adds a customer id, customer object
        and pin number to the bank's customer list as a dictionary."""
        cust_record = {
            "customer_id": customer_obj.get_name() + str(random.randint(0, 9999)).zfill(4),
            "details": customer_obj,
            "atm_pin": pin
        }
        self.customers.append(cust_record)
        

    def manages(self, atm_card_obj: object) -> None:
        """Accepts an ATM card object and adds it to the bank's ATM card list."""
        self.atm_cards.append(atm_card_obj)


    def maintains(self, atm_obj: object) -> None:
        """Accepts an atm object and stores it in the bank's ATM list."""
        self.atms.append(atm_obj)


    def authorize_pin(self, customer_obj: object, pin: str) -> bool:
        """Check if the provided pin matches the customer's pin.
        Returns True if the pin matches, raise an InvalidPinNumber exception otherwise."""
        for cust in self.customers:
            if customer_obj.get_name() == cust["details"].get_name() and cust["atm_pin"] == pin:
                return True
        raise InvalidPinNumber


    def get_acct(self, acct_num: str) -> object:
        """Returns account object if the account number is valid, otherwise
        raise an AccountNotFound exception"""
        for cust in self.customers:
            for account in cust["details"].get_acct_list():
                if account.get_acct_num() == acct_num:
                    return account
        raise AccountNotFound