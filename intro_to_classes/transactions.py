

class Transaction:
    def __init__(self, transaction_id, loan_id, amount, transaction_type):
        """Initialize transaction details."""
        self.transaction_id = transaction_id  # Unique transaction ID
        self.loan_id = loan_id  # Loan ID associated with the transaction
        self.amount = amount  # Payment or refund amount
        self.transaction_type = transaction_type  # "Payment" or "Refund"

    def display_transaction(self):
        """Display transaction details."""
        print("\n--- Transaction Details ---")
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Loan ID: {self.loan_id}")
        print(f"Amount: ${self.amount}")
        print(f"Transaction Type: {self.transaction_type}")
        print("----------------------\n")

# Test transaction system
if __name__ == "__main__":
    t1 = Transaction(1, 101, 500, "Payment")
    t2 = Transaction(2, 102, 200, "Refund")

    t1.display_transaction()
    t2.display_transaction()
