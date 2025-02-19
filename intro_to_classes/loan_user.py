class Loan:
    def __init__(self, loan_id, borrower, amount, interest_rate, duration):
        self.loan_id = loan_id
        self.borrower = borrower
        self.amount = amount
        self.interest_rate = interest_rate
        self.duration = duration  

    def calculate_total_amount(self):
        return self.amount + (self.amount * self.interest_rate * self.duration)

    def display_loan_details(self):
        print("\n--- Loan Details ---")
        print(f"Author: Srineha Saranu")  
        print(f"Loan ID: {self.loan_id}")
        print(f"Borrower: {self.borrower}")
        print(f"Amount: ${self.amount}")
        print(f"Interest Rate: {self.interest_rate * 100}%")
        print(f"Duration: {self.duration} years")
        print(f"Total Payable Amount: ${self.calculate_total_amount()}")
        print("----------------------\n")

# Get input from user
if __name__ == "__main__":
    loan_id = int(input("Enter Loan ID: "))
    borrower = input("Enter Borrower Name: ")
    amount = float(input("Enter Loan Amount: "))
    interest_rate = float(input("Enter Interest Rate (as decimal, e.g., 0.05 for 5%): "))
    duration = int(input("Enter Loan Duration (in years): "))

    # Create Loan object with user input
    user_loan = Loan(loan_id, borrower, amount, interest_rate, duration)
    user_loan.display_loan_details()
