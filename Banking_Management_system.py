class ATM:
    def __init__(self, money, users):
        self.money = money
        self.users = users
        self.current_user_id = None

    def login(self, user_id, password):
        if user_id in self.users and self.users[user_id]["password"] == password:
            self.current_user_id = user_id
            print("Login Successful.")
        else:
            print("Invalid credentials. Please try again.")

    def view_balance(self):
        if self.current_user_id is not None:
            return f"Your current balance is ${self.users[self.current_user_id]['balance']}"
        else:
            return "Please log in first."

    def withdraw(self, amount):
        if self.current_user_id is not None:
            remaining_amount = amount
            withdrawal = {}

            for note in sorted(self.money.keys(), reverse=True):
                if remaining_amount >= note:
                    count = min(remaining_amount // note, self.money[note])
                    withdrawal[note] = count
                    remaining_amount -= note * count
                    self.money[note] -= count

            if remaining_amount == 0:
                self.users[self.current_user_id]['balance'] -= amount
                return f"Withdrawal Successful: {withdrawal}. Your new balance is ${self.users[self.current_user_id]['balance']}"
            else:
                return "Insufficient funds or unable to provide requested denominations."
        else:
            return "Please log in first."


# Example Usage:
money = {2000: 5, 500: 20, 200: 20, 100: 34, 50: 20}
users = {62304: {"name": "parth", "password": 123, "balance": 50000}}

atm = ATM(money, users)

# Logging into the account
atm.login(62304, 123)

# Viewing balance
print(atm.view_balance())

# Withdrawing money from ATM
withdrawal_result = atm.withdraw(2500)
print(withdrawal_result)

# Viewing balance after withdrawal
print(atm.view_balance())



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