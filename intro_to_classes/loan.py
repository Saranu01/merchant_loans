
class Loan:
    def __init__(self, loan_id, borrower, amount, interest_rate, duration):
        """Initialize loan details."""
        self.loan_id = loan_id
        self.borrower = borrower
        self.amount = amount
        self.interest_rate = interest_rate
        self.duration = duration
        self.remaining_balance = self.calculate_total_amount()

    def calculate_total_amount(self):
        """Calculate total payable amount with interest."""
        return self.amount + (self.amount * self.interest_rate * self.duration)

    def make_payment(self, payment_amount):
        """Deduct payment from the remaining balance."""
        if 0 < payment_amount <= self.remaining_balance:
            self.remaining_balance -= payment_amount
            print(f"\n✅ Payment of ${payment_amount} successful!")
        else:
            print("\n❌ Invalid payment amount. Please enter a valid amount.")

    def display_loan_details(self):
        """Display loan information."""
        print("\n--- Loan Details ---")
        print(f"Loan ID: {self.loan_id}")
        print(f"Borrower: {self.borrower}")
        print(f"Total Loan Amount: ${self.calculate_total_amount()}")
        print(f"Remaining Balance: ${self.remaining_balance}")
        print("----------------------\n")


# List to store multiple loan objects
loans = []

def create_loan():
    """Create a new loan and add it to the list."""
    loan_id = int(input("Enter Loan ID: "))
    borrower = input("Enter Borrower Name: ")
    amount = float(input("Enter Loan Amount: "))
    interest_rate = float(input("Enter Interest Rate (as decimal, e.g., 0.05 for 5%): "))
    duration = int(input("Enter Loan Duration (years): "))

    loan = Loan(loan_id, borrower, amount, interest_rate, duration)
    loans.append(loan)
    print("\n✅ Loan Created Successfully!\n")

def make_payment():
    """Allow a user to make a payment towards a loan."""
    loan_id = int(input("Enter Loan ID to make a payment: "))
    for loan in loans:
        if loan.loan_id == loan_id:
            payment_amount = float(input("Enter payment amount: "))
            loan.make_payment(payment_amount)
            return
    print("\n❌ Loan ID not found!")

def view_loan_details():
    """View details of a specific loan."""
    loan_id = int(input("Enter Loan ID to view details: "))
    for loan in loans:
        if loan.loan_id == loan_id:
            loan.display_loan_details()
            return
    print("\n❌ Loan ID not found!")

def main():
    """Main menu to handle user actions."""
    while True:
        print("\n📌 Loan Management System")
        print("1. Create Loan")
        print("2. Make a Payment")
        print("3. View Loan Details")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            create_loan()
        elif choice == "2":
            make_payment()
        elif choice == "3":
            view_loan_details()
        elif choice == "4":
            print("\n🚀 Exiting Loan Management System. Thank you!")
            break
        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
