# import any necessary libraries/scripts here


class ATM_Card:
    def __init__(self, card_no: str, owned_by: object) -> None:
        self.__card_no = card_no
        self.__customer = owned_by

    def get_owned_by(self) -> object:
        """Getter for customer object"""
        return self.__customer

    def get_card_num(self) -> str:
        """Getter for card number"""
        return self.__card_no

    def __str__(self) -> str:
        """Returns string representation of ATM card with card number and owner's name."""
        return f"ATM Card Number: {self.get_card_num()}, Owned by: {self.get_owned_by().get_name()}"

    def get_acct_types(self) -> list:
        """Returns a list of the account types available for the customer"""
        acct_list = self.get_owned_by().get_acct_list()
        return [account.get_acct_type() for account in acct_list]

    def access(self, acct_type: str) -> object:
        """Accepts account type and returns the account object of the customer"""
        for account in self.get_owned_by().get_acct_list():
            if account.get_acct_type() == acct_type:
                return account
