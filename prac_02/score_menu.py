"""Provide a menu for working with a valid score."""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Run the score menu."""
    score = get_valid_score()

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell.")


def get_valid_score():
    """Get and return a score between 0 and 100 inclusive."""
    score = float(input("Score: "))

    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Score: "))

    return score


def determine_score(score):
    """Return the result category for a score."""
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


def print_stars(score):
    """Print one star for each whole point in the score."""
    print("*" * int(score))


main()