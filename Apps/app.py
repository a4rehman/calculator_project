import sys
from dbms import DBhelper
class Flipcart:

    def __init__(self):
        self.db=DBhelper()
        self.menu()

    def menu(self):
       user_input=input("""
        1.Enter 1 to register.
        2.Enter 2 to login.
        3.Enter 3 to exit.
        """)
       if user_input=='1':
           self.register()
       elif user_input=='2':
           self.login()
       elif user_input=='3':
           print("Thank you for using our Flipcart. Goodbye!")
           sys.exit(1000)
       else:
           print("Invalid choice. Please try again.")
    def register(self):
        print("Registering...")
    def login(self):
        print("Logging in...")


