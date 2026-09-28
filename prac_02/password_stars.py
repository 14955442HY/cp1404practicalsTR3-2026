"""Validate a password and display it as stars."""

MINIMUM_LENGTH = 8


def main():
    """Get a valid password and print matching stars."""
    password = get_password()
    print_stars(password)


def get_password():
    """Get and return a password of at least the minimum length."""
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters.")
        password = input("Password: ")
    return password


def print_stars(password):
    """Print one star for every character in the password."""
    print("*" * len(password))


main()