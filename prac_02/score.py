"""Determine results for user and random scores."""

import random


def main():
    """Display results for a user score and a random score."""
    user_score = float(input("Enter score: "))
    user_result = determine_score(user_score)

    print(f"User score {user_score} is {user_result}")

    if user_result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(0, 100)
    random_result = determine_score(random_score)
    print(f"Random: {random_score} = {random_result}")


def determine_score(score):
    """Return the result category for a score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


main()  