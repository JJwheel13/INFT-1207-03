# Author: Justin Wheeler (100982020)
# Completion Date: 2024-01-28
# Purpose: To perform Boundary Value Analysis and Robustness Testing in order to achieve an Expected Program Behavior

# Get_Input Function: Defines and Validates the Users Input, prevents values that aren't floats (aside from "calculate"), and values that aren't in range.
def get_input():
    # Prompt User for Input
    user_input = input("Enter Value: ")
    try:
        # Test for ValueError
        user_input = float(user_input)
        # Test for proper Range
        if -50 <= user_input <= 150:
            return user_input, True, False
        else:
            print("INVALID INPUT: Value must be between -50 and 150.")
            return user_input, False, False
    except ValueError:
        # Test if ValueError was for "calculate" prompt
        if user_input.lower().strip() == "calculate":
            return user_input, False, True
        else:
            print("INVALID INPUT: Value must be of a floating point integer.")
            return user_input, False, False

# Process_Output Function: Determines the Minimum, Maximum and Average values from a list of floats, before outputting these results to the user.
def process_output(temperatures:list):
    average_temperature = int()
    # Determine Minimum and Maximum
    minimum_temperature = min(temperatures)
    maximum_temperature = max(temperatures)
    # Determine Average
    for temperature in temperatures:
        average_temperature += temperature
    # Round off Average to two Decimal Places
    average_temperature = round((average_temperature/len(temperatures)), 2)

    # Output the results to the console
    print(f"\n----- [OUTPUT] -----\nMinimum Temperature: {minimum_temperature}°C\nMaximum Temperature: {maximum_temperature}°C\nAverage Temperature: {average_temperature}°C")

# Main Function: Manages the Console Interface, determining what functions to use and when to use them.
def main():
    # Define Variables
    temperature_list = list([])
    is_empty = bool()

    # Introduce the User to the Program
    print("----- [WELCOME] -----\nThis program performs various calculations\nbased on what you provide. Enter values\nbelow, and type \"calculate\" to continue.\n")
    # Loop the program until the list isn't empty, and the user has prompted the program to calculate using "calculate"
    while not is_empty:
        is_finished = bool()
        while not is_finished:
            # Determine the Users Input
            determined_input, is_valid, is_finished = get_input()
            if is_valid:
                # Add the validated Input to the list.
                temperature_list.append(determined_input)
        if len(temperature_list) != 0:
            is_empty = True
        else:
            print("INVALID INPUT: Provided List must not be empty.")

    # Calculate and Output the results to the Console
    process_output(temperature_list)

# Initialize Program
if __name__ == "__main__":
    # Redirect the starting point to Main()
    main()