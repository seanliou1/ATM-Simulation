# ATM simulation
This is a scaled down version of an Automated Teller Machine (ATM) using OOP principles. This is run on visual studio code.
Currentltly, the ATM can perform 4 operations:
1. Balance Enquiry
2. Cash withdrawals
3. Fund transfers
4. Quit

ATM transactions start only when the pin is entered correctly. If pin is invalid, the card is returned.
Each customer can have only 1 ATM card and each ATM card has access to both a customer's savings and current account (if any).
Each customer by default has a savings account.
Withdrawals operations are done from either the customer's savings or current account.
Transfer operations are done from either the customer's savings or current account, to another account. It could belong to the same customer or an account of another customer.
Transfer operations cannot go through if the transfer account number does not exist or if the transferer has insufficient funds.

## Assumptions
Each customer has either a savings account or both accounts when they open the accounts at a physical bank.
There is only 1 bank and 1 ATM currently, all other entities such as customer and accounts are allowed to have multiple objects.
Each customer has only 1 ATM card.

## Installation
Install visual studio code here (https://code.visualstudio.com/Download)
Install the Python extension and Python interpreter
Guide here (https://code.visualstudio.com/docs/languages/python)

Ensure all .py files are located in same folder

## Usage
When running the simulation, the ATM will first ask to choose 2 options:
1. Insert ATM card
2. Exit

Select 1 and enter card number, which will prompt the ATM to ask for pin next.
Enter the correct pin number to get to the main menu of transactions.
Card number and pin can be found in test_data.py and can be edited from there.

Current transactions available for this ATM as below:
1. Balance enquiry
2. Cash withdrawal
3. Fund transfer
4. Exit

## Test
```bash
python test_data.py run_sim
```
