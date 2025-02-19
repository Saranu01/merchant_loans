import sqlite3

class LoanDB:
    def __init__(self):
        self.conn = sqlite3.connect("bank.db")  # Create or connect to `bank.db`
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS loans (
                loan_id INTEGER PRIMARY KEY,
                borrower TEXT NOT NULL,
                amount REAL NOT NULL,
                interest_rate REAL NOT NULL,
                duration INTEGER NOT NULL,
                remaining_balance REAL NOT NULL
            )
        """)
        self.conn.commit()

    def add_loan(self, loan_id, borrower, amount, interest_rate, duration):
        total_payable = amount + (amount * interest_rate * duration)
        self.cursor.execute("""
            INSERT INTO loans (loan_id, borrower, amount, interest_rate, duration, remaining_balance) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (loan_id, borrower, amount, interest_rate, duration, total_payable))
        self.conn.commit()
        print("\n✅ Loan Added Successfully!")

    def make_payment(self, loan_id, payment_amount):
        self.cursor.execute("SELECT remaining_balance FROM loans WHERE loan_id = ?", (loan_id,))
        result = self.cursor.fetchone()
        if result:
            new_balance = result[0] - payment_amount
            self.cursor.execute("UPDATE loans SET remaining_balance = ? WHERE loan_id = ?", (new_balance, loan_id))
            self.conn.commit()
            print(f"\n✅ Payment of ${payment_amount} applied! New balance: ${new_balance}")
        else:
            print("\n❌ Loan ID not found!")

    def view_loan(self, loan_id):
        self.cursor.execute("SELECT * FROM loans WHERE loan_id = ?", (loan_id,))
        loan = self.cursor.fetchone()
        if loan:
            print("\n--- Loan Details ---")
            print(f"Loan ID: {loan[0]}")
            print(f"Borrower: {loan[1]}")
            print(f"Amount: ${loan[2]}")
            print(f"Interest Rate: {loan[3] * 100}%")
            print(f"Duration: {loan[4]} years")
            print(f"Remaining Balance: ${loan[5]}")
            print("----------------------\n")
        else:
            print("\n❌ Loan ID not found!")

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    db = LoanDB()

    while True:
        print("\n📌 Loan Management System")
        print("1. Add Loan")
        print("2. Make a Payment")
        print("3. View Loan Details")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            loan_id = int(input("Enter Loan ID: "))
            borrower = input("Enter Borrower Name: ")
            amount = float(input("Enter Loan Amount: "))
            interest_rate = float(input("Enter Interest Rate (as decimal, e.g., 0.05 for 5%): "))
            duration = int(input("Enter Loan Duration (years): "))
            db.add_loan(loan_id, borrower, amount, interest_rate, duration)
        elif choice == "2":
            loan_id = int(input("Enter Loan ID for payment: "))
            payment_amount = float(input("Enter payment amount: "))
            db.make_payment(loan_id, payment_amount)
        elif choice == "3":
            loan_id = int(input("Enter Loan ID to view details: "))
            db.view_loan(loan_id)
        elif choice == "4":
            db.close_connection()
            print("\n🚀 Exiting Loan Management System. Thank you!")
            break
        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 4.")

            from transactions1 import TransactionDB

from transactions1 import TransactionDB

def make_payment(self, loan_id, payment_amount):
    self.cursor.execute("SELECT remaining_balance FROM loans WHERE loan_id = ?", (loan_id,))
    result = self.cursor.fetchone()

    if result:
        new_balance = result[0] - payment_amount
        self.cursor.execute("UPDATE loans SET remaining_balance = ? WHERE loan_id = ?", (new_balance, loan_id))
        self.conn.commit()

        # Debugging - Print transaction being saved
        print(f"\n🔍 Debug: Recording payment transaction for Loan ID {loan_id} - Amount: ${payment_amount}")

        # Record the transaction
        transaction_db = TransactionDB()
        transaction_db.record_transaction(loan_id, payment_amount, "Payment")
        transaction_db.close_connection()

        print(f"\n✅ Payment of ${payment_amount} applied! New balance: ${new_balance}")
    else:
        print("\n❌ Loan ID not found!")


