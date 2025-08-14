# import any necessary libraries/scripts here
from datetime import datetime

class Customer:
    def __init__(self, name: str, addr: str, dob: str) -> None:
        self.__name = name
        self.__address = addr
        self.__dateofbirth = datetime.strptime(dob, "%d-%b-%Y") #(DD-MMM-YYYY)
        self.__acc_list = []

    def __str__(self) -> str:
        """Returns a string representation of the customer detailing the
        name, address, and date of birth."""
        return f"Customer name: {self.get_name()}, \
Address: {self.__address}, \
Date of birth: {self.__dateofbirth.strftime("%d-%b-%Y")}"

    def owns(self, acct_obj: object) -> None:
        """Accepts an account object and adds it to the customer's account list."""
        self.get_acct_list().append(acct_obj)

    def get_name(self) -> str:
        """Getter for the customer's name."""
        return self.__name

    def get_acct_list(self) -> list:
        """Getter for the customer's account list."""
        return self.__acc_list
