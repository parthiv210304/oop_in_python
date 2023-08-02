class Atm:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin

    def check_pin(self):
        entered_pin = int(input("Enter your pin: "))
        return entered_pin == self.pin

    def change_pin(self):
        new_pin = int(input("Enter the new pin: "))
        self.pin = new_pin
        print("Pin changed successfully.")

    def deposit(self):
        amount = int(input("Enter the amount you want to deposit: "))
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self):
        amount = int(input("Enter the value you want to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Not enough balance.")

    def check_balance(self):
        print("Your balance is:", self.balance)

    def start(self):
        while True:
            user_input = int(input("""
                1. Press 1 to change pin.
                2. Press 2 to deposit.
                3. Press 3 to withdraw.
                4. Press 4 to check balance.
                5. Press 5 to exit.
                """))

            if user_input == 1:
                if self.check_pin():
                    self.change_pin()
                else:
                    print("Incorrect pin.")
            elif user_input == 2:
                if self.check_pin():
                    self.deposit()
                else:
                    print("Incorrect pin.")
            elif user_input == 3:
                if self.check_pin():
                    self.withdraw()
                else:
                    print("Incorrect pin.")
            elif user_input == 4:
                if self.check_pin():
                    self.check_balance()
                else:
                    print("Incorrect pin.")
            elif user_input == 5:
                print("Thanks for visiting us.")
                break
            else:
                print("Invalid input. Please try again.")


sbi = Atm(1234)
sbi.start()
