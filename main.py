class Atm:
    def __init__(self,pin):
        self.balance = 0
        self.pin = pin

    user_input = int(input(""""
                           1.Press 1 to change pin.
                           2.Press 2 to deposit.
                           3.Press 3 to withdraw.
                           4.Press 4 to check balance.
                           5.Press 5 to exit.                       """))
    
    while True:
        def check_pin(self):
            pin = int(input("Enter your pin: "))
            return pin == self.pin

        def change_pin(self):
            
            new_pin = int(input("Enter the new pin: "))
            self.pin = new_pin

        def deposit(self):
            amount = int(input("Enter the amount you want to deposit: "))
            self.balance = self.balance + amount

        def withdraw(self):
            amount = int(input("Enter the value you want to withdraw: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
            else:
                print("Not enough balance")

        def check_balance(self):
            print("Your balance is: ",self.balance)
        if user_input == 1:
            check_pin()
            if check_pin:
                change_pin()
            else:
                print("Incorrect pin.")
        if user_input== 2:
            check_pin()
            if check_pin:
                deposit()
            else:
                print("Incorrect pin.")
        if user_input== 3:
            check_pin()
            if check_pin:
                withdraw()
            else:
                print("Incorrect pin.")
        if user_input== 4:
            check_pin()
            if check_pin:
                check_balance()
            else:
                print("Incorrect pin.")
        if user_input== 5:
            print("Thanks for visiting us.")
            break
    
     
sbi = Atm(1234)
