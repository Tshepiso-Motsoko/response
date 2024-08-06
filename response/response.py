import sys
from validators import email


def main():
    # Prompt the user for an email address
    email_address = input("What's your email address? ")

    # Validate the email address using the email function from validators
    if email(email_address):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
