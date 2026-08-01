class Account:
    def __init__(self, account_id, balance=0.0):
        self.account_id = account_id
        self.balance = balance
        self.transaction_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_count += 1

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_count += 1
            return True  # withdrawal succeeded
        else:
            return False  # withdrawal declined


class Ledger:
    def __init__(self):
        self.diff_accounts = {}
        self.flagged = []

    def get_or_create(self, account_id):
        if account_id not in self.diff_accounts:
            self.diff_accounts[account_id] = Account(account_id)
        return self.diff_accounts[account_id]

    def apply(self, account_id, transact_type, amount):
        account = self.get_or_create(account_id)

        if transact_type == "deposit":
            account.deposit(amount)
        elif transact_type == "withdraw":
            success = account.withdraw(amount)
            if not success:
                self.flagged.append({
                    "account_id": account_id,
                    "amount": amount
                })

    def summary(self):
        return {
            "accounts": self.diff_accounts,
            "flagged": self.flagged
        }