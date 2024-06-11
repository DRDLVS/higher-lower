# hacer que se vaya recorriendo solo puede salir 2 veces la misma cosa
# hacer un score cada vez que le atinen
# en el momento que no acierten, pierden


from art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)

# -------------------------------------------------------------------
def get_random_account():
    """Get data from a random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# -------------------------------------------------------------------
def game():
    score = 0
    game_should_continue = True

    # Initialize accounts A and B
    account_a = get_random_account()
    account_b = get_random_account()

    while account_a == account_b:
        account_b = get_random_account()

    while game_should_continue:
        # Display account information
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Get user input
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Get follower counts
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if the user's guess is correct
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear the screen and display the logo
        clear()
        print(logo)

        if is_correct:
            score += 1
            print(f"Correct! Your current score is: {score}.")
            # B becomes the new A
            account_a = account_b
            account_b = get_random_account()
            while account_a == account_b:
                account_b = get_random_account()
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

# Run the game
game()
