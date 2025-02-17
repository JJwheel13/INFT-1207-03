# Author: Justin Wheeler 100982020
# Completion Date: 2025-01-29
# Purpose: To retrieve, validate, and calculate a list of temperatures provided by the user

# Import Libraries
import PySimpleGUI as sg
import statistics

# validate_temperature Function: Validates the list of temperatures
def validate_temperature(value):
    # Attempt Text-Conversion
    try:
        value = eval(value, {}, {})
        # Validate proper Data-Type and Scope
        if isinstance(value, (int, float)) and -50 <= value <= 150:
            return value
        else:
            return None
    # Throw Exception (Invalid Datatype, Invalid Syntax, Invalid Name, Invalid Type)
    except (ValueError, SyntaxError, NameError, TypeError):
        return None

# process_temperatures Function: Processes a list of temperatures provided by the user, filters into a proper list
def process_temperatures(temp_list):
    valid_temps = []
    # Loop through inputted temperatures
    for temp in temp_list:
        # Validate selected temperature
        valid_temp = validate_temperature(temp)
        if valid_temp is not None:
            # Add Validated Temperature to the List
            valid_temps.append(valid_temp)

    # Throw Exception in GUI: (Invalid Input)
    if not valid_temps:
        return "No valid input provided."

    # Calculate Minimum, Maximum, and Average Temperatures based on the filtered list
    min_temp = min(valid_temps)
    max_temp = max(valid_temps)
    avg_temp = round(statistics.mean(valid_temps), 2)

    # Output the filtered list to the console
    return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"


# GUI Layout
sg.theme("DarkTeal6")

layout = [
    [sg.Text("Enter Temperature Readings (°C):")],
    [sg.InputText(key="-TEMP1-"), sg.InputText(key="-TEMP2-"), sg.InputText(key="-TEMP3-")],
    [sg.Button("Process"), sg.Button("Clear"), sg.Button("Exit")],
    [sg.Text("", size=(40, 1), key="-OUTPUT-")]
]

window = sg.Window("Temperature Sensor Processor", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Process":
        temp_inputs = [values["-TEMP1-"], values["-TEMP2-"], values["-TEMP3-"]]
        result = process_temperatures(temp_inputs)
        window["-OUTPUT-"].update(result)

    if event == "Clear":
        window["-TEMP1-"].update("")
        window["-TEMP2-"].update("")
        window["-TEMP3-"].update("")
        window["-OUTPUT-"].update("")

window.close()