# Author: Justin Wheeler (100982020)
# Completion Date: 2025-01-14
# Purpose: To handle, calculate with, and utilize file output with a list of movies with their information.

# Import Libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import *

# Construct Window
window = Tk()
# Define Title
window.title("Movie Manager")

# Define Variables
selectedOption = tk.StringVar()
selectedOption.set("Add Movie")
options = ["Add Movie", "Remove Movie", "Calculate Results"]

# Define Functions
# Validation Function: Defines if GUI inputs are valid for adding/removing functions.
def validate_input(name_input:str, budget_input:str, validation_type:str):
    # Determine function usage.
    match validation_type:
        # Validate if both Name and Budget fields we're inputted and are of proper format.
        case "add":
            try:
                budget_input = int(budget_input)
                if name_input != "":
                    # Display function success.
                    messagebox.showinfo("Movie Addition", "Added {} Successfully.".format(name_input))
                    return True
            except:
                # Display function fail.
                messagebox.showwarning("Invalid Input", "Both the Name and the Budget of the Movie must be specified.")
                return False
        # Validate if only the Name field was inputted and is of proper format.
        case "remove":
            if budget_input != "":
                messagebox.showwarning("Invalid Input", "Budget should not be specified in removal.")
                return False
            elif name_input != "":
                messagebox.showinfo("Movie Removal", "Removed {} Successfully.".format(name_input))
                return True
            else:
                messagebox.showwarning("Invalid Input", "Movie Name should be specified.")
                return False

# Determine Selection Function: Determines the function the user has attempted to utilize.
def determine_selection():
    # Determine option selected.
    match selectedOption.get():
        # Call Functions, pass relevant values.
        case "Add Movie":
            add_movie(entryNameBox.get(), entryBudgetBox.get())
        case "Remove Movie":
            remove_movie(entryNameBox.get(), entryBudgetBox.get())
        case "Calculate Results":
            calculate_results()

# Add Movie Function: Adds a movie (name and budget) to the Movie List (movielist.txt).
def add_movie(name_input:str, budget_input:str):
    # Determine validation success.
    if validate_input(name_input, budget_input, "add"):
        # Append Movie to the list.
        with open ("movielist.txt", "a") as file:
            file.write("\n(\"{}\", {})".format(name_input, budget_input))

# Remove Movie Function: Removes a movie from the Movie List (movielist.txt).
def remove_movie (name_input:str, budget_input:str):
    # Determine validation success.
    if validate_input(name_input, budget_input, "remove"):
        # Store all lines from the Movie List
        with open ("movielist.txt", "r") as file:
            lines = file.readlines()
        # Rewrite the file using the stored Movie List, exclude any lines that match the users selection.
        with open ("movielist.txt", "w") as file:
            for line in lines:
                selected_line = eval(line.strip())
                if selected_line[0] != name_input:
                    file.write(line)

# Calculate Results Function: Determines the Average Budget, Movies that have an above-average Budget, and Movies sorted by the Budget. Prints the results to the console and output.txt file.
def calculate_results():
    # Create Variables.
    tuple_list = []
    average_budget = float()
    # Convert lines from the movie list into a list of tuples.
    with open ("movielist.txt", "r") as file:
        for line in file:
            tuple_list.append(eval(line.strip()))
    # Tally all budgets from the Movie List to determine the Average Budget.
    for selected_budget in tuple_list:
        average_budget += selected_budget[1]
    average_budget = average_budget/(len(tuple_list)-1)
    print("Average Budget: {:.2f}\n\nMovies with above-average Budget:".format(average_budget))
    with open ("output.txt", "w") as file:
        file.write("Average Budget: {:.2f}\n\nMovies with above-average Budget:".format(average_budget))
    # Display movies that are above the Average Budget.
    for selected_tuple in tuple_list:
        if (average_budget - selected_tuple[1]) >= 0:
            print("{}: ${} (Higher by ${:.2f})".format(selected_tuple[0], selected_tuple[1], (average_budget - selected_tuple[1])))
            with open ("output.txt", "a") as file:
                file.write("\n{}: ${} (Higher by ${:.2f})".format(selected_tuple[0], selected_tuple[1], (average_budget - selected_tuple[1])))
    print("\nMovies Sorted by Budget (Ascending):")
    with open ("output.txt", "a") as file:
        file.write("\n\nMovies Sorted by Budget (Ascending):")
    # Sort the Movie List specifically by each tuples respective Budget (descending order).
    tuple_list.sort(key=lambda x: x[1])
    # Display movies that are sorted by their respective Budgets (descending order).
    for selected_tuple in tuple_list:
        print("{}: ${}".format(selected_tuple[0], selected_tuple[1]))
        with open ("output.txt", "a") as file:
            file.write("\n{}: ${}".format(selected_tuple[0], selected_tuple[1]))
    print("\nResults written to file \"output.txt\".")

# Define Widgets
labelTitleText = Label(window, text="Movie Manager", font=("Helvetica", 24, "bold"))
labelNameText = Label(window, text="Movie Name:", font=("Helvetica", 11))
labelBudgetText = Label(window, text="Movie Budget:", font=("Helvetica", 11))
entryNameBox = Entry(window, width=30)
entryBudgetBox = Entry(window, width=30)
dropdownSelectionBox = OptionMenu(window, selectedOption, *options)
buttonSubmission = Button(window, text="Submit", command=determine_selection)

# Place Widgets
labelTitleText.grid(row=0,column=1)
labelNameText.grid(row=1,column=0)
entryNameBox.grid(row=1,column=1)
dropdownSelectionBox.grid(row=1,column=2)
labelBudgetText.grid(row=2,column=0)
entryBudgetBox.grid(row=2,column=1)
buttonSubmission.grid(row=2,column=2)

# Initialize Program
window.mainloop()