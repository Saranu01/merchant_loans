import sqlite3

class TransactionDB:
    def __init__(self):
        """Connect to database and create transactions table if not exists."""
        self.conn = sqlite3.connect("bank.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                loan_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                transaction_type TEXT NOT NULL,
                transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (loan_id) REFERENCES loans (loan_id)
            )
        """)
        self.conn.commit()

    def record_transaction(self, loan_id, amount, transaction_type):
        """Insert a transaction into the database."""
        self.cursor.execute("""
            INSERT INTO transactions (loan_id, amount, transaction_type) 
            VALUES (?, ?, ?)
        """, (loan_id, amount, transaction_type))
        self.conn.commit()
        print("\n✅ Transaction Recorded Successfully!")

    def view_transactions(self, loan_id):
        """Retrieve all transactions for a loan."""
        self.cursor.execute("SELECT * FROM transactions WHERE loan_id = ?", (loan_id,))
        transactions = self.cursor.fetchall()
        if transactions:
            print("\n--- Transaction History ---")
            for t in transactions:
                print(f"Transaction ID: {t[0]}, Amount: ${t[2]}, Type: {t[3]}, Date: {t[4]}")
            print("----------------------\n")
        else:
            print("\n❌ No transactions found for this Loan ID!")

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()
if __name__ == "__main__":
    db = TransactionDB()  # Create database connection

    loan_id = int(input("Enter Loan ID to view transactions: "))  # Get Loan ID from user
    db.view_transactions(loan_id)  # View transactions for that Loan ID

    db.close_connection()  # Close database connection
