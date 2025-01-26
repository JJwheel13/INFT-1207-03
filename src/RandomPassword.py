# Import Libraries
import random
import string

# Get_User_Input Function: Retrieves and Validates User Input for Password Generation
def get_user_input(): # Karim
    while True:
        try:
            total_length = int(input("Enter the total length of the password: "))
            if total_length < 8:
                print("Please enter a value of greater than or equal to 8 to create a secure password.")
                continue

            letters = int(input("Enter the number of letters desired in the password: "))
            digits = int(input("Enter the number of digits desired in the password: "))
            special_chars = int(input("Enter the number of special characters desired in the password: "))

            if letters < 0 or digits < 0 or special_chars < 0:
                print("Please enter non-negative values for letters, digits, and special characters.")
                continue

            if letters + digits + special_chars > total_length:
                print(
                    "The sum of letters, digits, and special characters exceeds the total length. Please enter valid values.")
                continue

            total_length = letters + digits + special_chars

            return total_length, letters, digits, special_chars
        except ValueError:
            print("Invalid input. Please enter integers only.")

# Generate_Password Function: Generates a Secure Password based on user-specified criteria
def generate_password(total_length, letters, digits, special_chars): # Justin
    # Generate required characters
    chosen_letters = random.choices(string.ascii_letters, k=letters)
    chosen_digits = random.choices(string.digits, k=digits)
    chosen_specials = random.choices(string.punctuation, k=special_chars)

    # Fill the rest of the password with random characters (if needed)
    remaining_chars = total_length - (letters + digits + special_chars)
    chosen_remaining = random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_chars)

    # Combine all characters and shuffle
    password_list = chosen_letters + chosen_digits + chosen_specials + chosen_remaining
    random.shuffle(password_list)

    # Return the final password as a string
    return ''.join(password_list)

# Main Function: Directs processes and outputs final results
def main():
    # Retrieve User Input
    total_length, letters, digits, special_chars = get_user_input()

    # Generate Password
    password = generate_password(total_length, letters, digits, special_chars)

    # Output the Results to the User
    print("\nYour desired password is:", password)
    print("Password successfully generated with:")
    print(f"- Letters: {letters}")
    print(f"- Digits: {digits}")
    print(f"- Special characters: {special_chars}")

# Initialize the Program
if __name__ == "__main__":
    main()