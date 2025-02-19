

class Loan:
    def __init__(self, loan_id, borrower, amount, interest_rate, duration):
       
        self.loan_id = loan_id
        self.borrower = borrower
        self.amount = amount
        self.interest_rate = interest_rate
        self.duration = duration  # in years

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



if __name__ == "__main__":
    loan1 = Loan(101, "Meghana", 5000, 0.05, 3)
    loan1.display_loan_details()

    loan2 = Loan(102, "Lahari", 8000, 0.06, 4)
loan2.display_loan_details()

