"""
Demonstration: Arbitrary Keyword Arguments (**kwargs) and formatted dictionary printing.

Author: Moulika Routhu
"""

def person(**data):
    """
    Prints the dictionary items passed using **kwargs with clean formatting.
    Only prints fname, lname, age, and phno if present.
    """
    for key, value in data.items():
        print(f"{key:<6}: {value}")  # Align keys to 6 characters for neat output

# Example call with known data to test functionality
print("\n--- Printing Example Data ---")
person(
    fname='kirankumar',
    lname='routhu',
    age=18,
    phno='9652630360'
)

# Taking user input repeatedly using **kwargs and while loop
print("\n--- User Data Entry ---")

while True:
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    age = input("Enter your age: ")
    phno = input("Enter your mobile number: ")

    print("\n--- Entered User Data ---")
    person(
        fname=fname,
        lname=lname,
        age=age,
        phno=phno
    )

    exit_choice = input("\nEnter 0 to exit or any key to continue: ")
    if exit_choice == '0':
        print("\nExiting user data entry. Thank you!\n")
        break
