"""
Member Management System
Author: Srineha Saranu
Date: February 2025
Description: Manages borrowers (loan members) with details like name, ID, and contact info.
"""

class Member:
    def __init__(self, member_id, name, email, phone):
        """Initialize member details."""
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone

    def display_member_details(self):
        """Display borrower (member) details."""
        print("\n--- Member Details ---")
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print("----------------------\n")

# Test the Member class
if __name__ == "__main__":
    member1 = Member(1, "Meghana", "meghana@email.com", "123-456-7890")
    member2 = Member(2, "Lahari", "lahari@email.com", "987-654-3210")

    member1.display_member_details()
    member2.display_member_details()
