class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.min_withdrawal = 100
        self.max_withdrawal = 10000

    def check_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            return False, "Invalid deposit amount. Please enter a positive value."
        
        self.balance += amount
        print(f"Amount Deposited: ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")
        return True, ""

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Invalid deposit amount. Please enter a positive value."
        
        if amount < self.min_withdrawal:
            return False, f"Minimum withdrawal amount is ${self.min_withdrawal}"
            
        if amount > self.max_withdrawal:
            return False, f"Maximum withdrawal amount is ${self.max_withdrawal}"
            
        if amount > self.balance:
            return False, "Insufficient funds"
            
        self.balance -= amount
        print(f"Amount Withdrawn: ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")
        return True, ""

def main():
    atm = ATM(1000)
    
    while True:
        print("\nWelcome to ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        try:
            choice = int(input("\nSelect Option: "))
            print()
            
            if choice == 1:
                atm.check_balance()
                
            elif choice == 2:
                try:
                    amount = float(input("Enter amount: $"))
                    success, message = atm.deposit(amount)
                    if not success:
                        print(message)
                except ValueError:
                    print("Please enter a valid amount")
                    
            elif choice == 3:
                try:
                    amount = float(input("Enter amount: $"))
                    success, message = atm.withdraw(amount)
                    if not success:
                        print(message)
                except ValueError:
                    print("Please enter a valid amount")
                    
            elif choice == 4:
                print("Thank you for using ATM")
                break
                
            else:
                print("Invalid option")
                
        except ValueError:
            print("Please select a valid option")

if __name__ == "__main__":
    main()
