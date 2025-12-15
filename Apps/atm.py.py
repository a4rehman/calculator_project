from email.utils import UEMPTYSTRING


class Atm:
    def __init__(self):
        self.__pin = ''
        self.__balance = 0

    def menu(self):
        while True:
            user_input = input('''
            Hello! How would you like to proceed?
            1. Press 1 to create a PIN code.
            2. Press 2 to deposit cash.
            3. Press 3 to withdraw.
            4. Press 4 to check balance.
            5. Press 5 to exit.
            Enter your choice: ''')

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_pin(self):
        if self. __pin is  UEMPTYSTRING:
             self.__pin = input("Enter your new PIN code: ")
             print("PIN created successfully.")
        else:
            temp=input("Enter your old pin code first.")
            if temp==self. __pin:
                self.__pin = input("Enter your new PIN code: ")
                print("PIN created successfully.")
            else:
                print("please enter correct pin code.")

    def deposit(self):
        temp_pin = input("Enter your PIN code: ")
        if temp_pin == self.__pin:
            amount = int(input("Enter the amount to deposit: "))
            if amount > 0:
                self.__balance += amount
                print(f"Your cash has been deposited successfully. New balance: {self.__balance}")
            else:
                print("Invalid amount. Please enter a positive number.")
        else:
            print("You entered the wrong PIN code.")

    def withdraw(self):
        temp_pin = input("Enter your PIN code: ")
        if temp_pin == self.__pin:
            amount = int(input("Enter the withdrawal amount: "))
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"Your cash has been withdrawn successfully. Remaining balance: {self.__balance}")
            else:
                print("Invalid amount or insufficient balance.")
        else:
            print("You entered the wrong PIN code.")

    def check_balance(self):
        temp_pin = input("Enter your PIN code: ")
        if temp_pin == self.__pin:
            print(f"Balance of your account: {self.__balance}")
        else:
            print("You entered the wrong PIN code.")


# Run the ATM system
atm = Atm()
atm.menu()
