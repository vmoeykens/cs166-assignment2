"""
Authentication Script to Test
CS166 - Cybersecurity Principles

"""

import json
import sys

# Set maximum number of attempts to login
MAX_ATTEMPTS = 3
# Special characters to test password strength
SPECIAL_CHAR = "!@#$%^&*"
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 50


def menu():
    """
    Display program splash screen, get menu choice from user
    Route to selected function.
    """
    option = display_welcome_screen()
    if option == 1:
        authenticate()
    elif option == 2:
        new_user()
    elif option == 3:
        program_exit()


def display_welcome_screen() -> int:
    """
    Display splash screen at program startup. Get user menu choice

    :return: choice: int
    """
    border = "\n" + "*" * 20 + "\n"
    print(border + "Secure System Access" + border)
    print("Please select from the following options: \n")
    print("\t1. Login")
    print("\t2. New User Account")
    print("\t3. Quit\n")
    try:
        choice = int(input(">>> "))
        if choice not in [1, 2, 3]:
            print("\nInvalid option.\n")
            menu()
    except ValueError:
        print("\nInvalid option.\n")
        menu()
    else:
        return choice


def authenticate():
    """
    Authenticate function prompts user for a username and  password, tests them
    against the stored credentials and calls the logged_in function if the password
    matches for a given user. The user is permitted 3 attempts to correctly enter
    their password.
    """
    border = "\n" + "*" * 10 + "\n"
    print(border + "Login Menu" + border)

    # Initialize values
    password_match = False
    attempts = 0

    # Prompt user for pw, compare to pw stored in "database"
    while not password_match and attempts < MAX_ATTEMPTS:

        # Get password from user
        user_name = input("Enter your username: ")
        while user_name == "":
            user_name = input("Enter your username: ")

        user_password = input("Enter your password: ")
        while user_password == "":
            user_password = input("Enter your password: ")

        # Compare entered credentials to the stored credentials
        password_match = database(user_name, user_password)

        # Login user if authorized
        if password_match:
            logged_in()
        else:
            print("\t** Username and/or Password incorrect. **\n")
            attempts += 1
            if attempts == MAX_ATTEMPTS:
                print(f"\tThat was {MAX_ATTEMPTS} invalid attempts.")
                print("\t** You are locked out of the system. **\n")
                sys.exit()


def database(un, pw) -> bool:
    """
    Database simulator function. Check user supplied credentials against
    credentials stored in json file. Return true if un/pw matches, false
    otherwise.

    :param un: str
    :param pw: str
    :return: bool
    """
    try:
        with open("database.json", "r") as f:
            credentials = json.load(f)
            if credentials[un] == pw:
                return True
            else:
                return False
    except KeyError:
        return False
    except IOError:
        print("Error reading file. Aborting...")
        sys.exit()
    except json.decoder.JSONDecodeError:
        print("Error reading file. Aborting...")
        sys.exit()


def new_user():
    """ Register new user """
    border = "\n" + "*" * 13 + "\n"
    print(border + "New User Menu" + border)

    try:
        with open("database.json", "r") as f:
            credentials = json.load(f)

        # Get desired credentials from user
        user = input("Select your username: ")
        while user in credentials:
            print("\t** Sorry, that username already exists. **\n")
            user = input("Select your username: ")

        password = input("Select your password: ")
        while not password_strength(password):
            print("\t** Sorry, password not complex enough. **\n")
            password = input("Enter a new password: ")

        # Write updated dictionary to file
        credentials[user] = password
        with open("database.json", "w") as f:
            json.dump(credentials, f, indent=2)

        print("\n** Account successfully created. **\n")
        menu()
    except IOError:
        print("Error reading file. Aborting...")
        sys.exit()
    except json.decoder.JSONDecodeError:
        print("Error reading file. Aborting...")
        sys.exit()


def password_strength(test_password) -> bool:
    """
    Check basic password strength. Return true if password
    meets minimum complexity criteria, false otherwise.

    :param test_password: str
    :return: bool
    """
    if test_password.isalnum() or test_password.isalpha():
        return False
    if len(test_password) < PASSWORD_MIN_LENGTH:
        return False
    if len(test_password) > PASSWORD_MAX_LENGTH:
        return False
    special_char_check = False
    has_upper = False
    has_lower = False
    has_digit = False
    for ch in test_password:
        if ch in SPECIAL_CHAR:
            special_char_check = True
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True
    if not special_char_check or \
            not has_upper or \
            not has_lower or \
            not has_digit:
        return False
    else:
        return True


def program_exit():
    """ Confirm user intends to exit, then quits if yes"""
    print("\nAre you sure you want to exit? (y/n)")
    quit_choice = input(">>> ")

    while quit_choice.lower() != "y" and quit_choice.lower() != "n":
        print("\nInvalid option.\n")
        print("Are you sure you want to exit? (y/n)")
        quit_choice = input(">>> ")
    if quit_choice.lower() == "y":
        print("\nThank you for using the top secret system.")
        sys.exit()
    else:
        menu()


def logged_in():
    """ Message to display if user enters correct credentials """
    print("\nWelcome to the top secret system.")


# Call main function
if __name__ == '__main__':
    menu()