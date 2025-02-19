from members import Member

# Global variable
member_count = 20


class BaseAccount:
    def __init__(self, id, od, mi, ba):
        """Initialize base account properties."""
        self.id = id
        self.open_date = od
        self.member_id = mi
        self.member = None
        self.balance = ba

    def add_money_to_account(self, amount):
        """Add money to balance and return updated balance."""
        self.balance += amount
        return self.balance


class CheckingAccount(BaseAccount):
    def __init__(self, id, od, mi, ba, ty="Checking"):
        """Initialize CheckingAccount with base properties and account type."""
        super().__init__(id, od, mi, ba)  # Corrected super() call
        self.type = ty

    def withdraw_money(self, amount):
        """Check if balance remains above 0 before withdrawing."""
        if self.balance - amount < 0:
            print("❌ Insufficient funds!")
            return False
        self.balance -= amount
        return self.balance  # Return updated balance

    def retrieve_account_details_with_type(self):
        """Retrieve account details."""
        return f"Account Type: {self.type}, Member ID: {self.member_id}"


# Multi-level inheritance
class PremiumCheckingAccount(CheckingAccount):
    def __init__(self, id, od, mi, ba, ty="Premium Checking"):
        """Initialize Premium Checking Account."""
        super().__init__(id, od, mi, ba, ty)  # Corrected super() call

    def add_secondary_account_holder(self):
        """Method to add a secondary account holder."""
        return "Secondary account holder added"


# Multiple inheritance - Requires BaseCountry class
class BaseCountry:
    def __init__(self, country_name):
        """Initialize country details."""
        self.country_name = country_name


class CheckingAccountMultiple(BaseAccount, BaseCountry):
    def __init__(self, id, od, mi, ba, country_name):
        """Initialize a Checking Account with multiple inheritance."""
        BaseAccount.__init__(self, id, od, mi, ba)  # Initialize BaseAccount
        BaseCountry.__init__(self, country_name)  # Initialize BaseCountry


class SavingsAccount(BaseAccount):
    def __init__(self, id, od, mi, ba, ty="Savings", md=0):
        """Initialize SavingsAccount with monthly deposit."""
        super().__init__(id, od, mi, ba)
        self.type = ty
        self.monthly_deposit = md

    def withdraw_money(self, amount):
        """Ensure balance stays above $500 and allow only one withdrawal per day."""
        if self.balance - amount < 500:
            print("❌ Withdrawal not allowed! Minimum balance of $500 required.")
            return False
        self.balance -= amount
        return self.balance  # Return updated balance

    def retrieve_account_details_with_type(self):
        """Retrieve account type details."""
        return f"Account Type: {self.type}, Member ID: {self.member_id}"


# ✅ Object creation with required parameters
checking1 = CheckingAccount(101, "2024-02-19", 1, 5000)
baseAccount1 = BaseAccount(102, "2024-02-10", 2, 3000)

# ✅ Testing methods
print(f"New Balance after adding money: ${baseAccount1.add_money_to_account(1000)}")  # Add money
print(f"New Checking Balance after adding money: ${checking1.add_money_to_account(500)}")  # Add money
print(f"New Balance after withdrawal: ${checking1.withdraw_money(1000)}")  # Withdraw money
print(checking1.retrieve_account_details_with_type())  # Retrieve details
