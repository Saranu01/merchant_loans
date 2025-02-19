class Member:
    """Class representing a bank member."""

    member_serial_number = 0  # Class variable

    def __init__(self, email, fname=None, lname=None, age=None, address=None, salary=None):
        """Initialize Member object."""
        self.id = None
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.phone_number = None
        self.age = age
        self.address = address
        self.salary = salary
        self.__ssn = None  # Private attribute

    @staticmethod
    def retrieve_serial_number_static():
        """Retrieve static serial number."""
        return Member.member_serial_number

    @classmethod
    def retrieve_serial_number_class(cls):
        """Retrieve serial number using class method."""
        return cls.member_serial_number  # Can also use Member.member_serial_number

    # Private method
    def __retrieve_ssn(self):
        """Retrieve Social Security Number (SSN) (Private Method)."""
        print(self.__ssn)

    def retrieve_member_details(self):
        """Retrieve member details from the database using email."""
        member_serial_number = 20  # Local variable
        return "Member details retrieved"

    def create_new_member(self):
        """Save new member to database and raise an exception if email already exists."""
        return "ID of inserted row"


# ✅ Corrected Object Creation
new_member = Member("test@example.com", fname="John", lname="Doe", age=30, address="123 Street", salary=50000)

# ✅ Printing Class & Instance Attributes
print(new_member.member_serial_number)  # ✅ Valid (access class variable from instance)
print(Member.member_serial_number)  # ✅ Valid (access class variable from class)

print(new_member.first_name)  # ✅ Valid (access instance variable)
# print(Member.first_name)  # ❌ ERROR: Instance variable cannot be accessed via class

# ✅ Calling Static & Class Methods
print(Member.retrieve_serial_number_class())  # ✅ Correct way to call class method
print(new_member.retrieve_serial_number_static())  # ✅ Correct way to call static method

# ✅ Accessing Private Methods Using Name-Mangling
new_member._Member__retrieve_ssn()  # ✅ Correct way to access private method
