from graphics import *  # Import the graphics library

TOTAL_CREDITS = 120  # Total of the pass credits
PASS_CREDITS = [120, 100, 80, 60, 40, 20, 0]  # Valid range

# Function to validate inputs (Check that the input is an integer and within the valid range)
"""
    reference: https://www.w3schools.com/python/python_operators.asp
"""


def validate_input(num, valid_range=None):  # valide_range is maximum valid value
    try:
        num = int(num)  # Convert input to an integer
        if valid_range is not None and num not in valid_range:  # Check if the input is in the valid range
            print("Out of range.")
            return None  # Return None if the input is not in the valid range
        return num  # Return the input if it is valid
    except ValueError:  # If the input is not an integer
        print("Integer required.")
        return None  # Return None if the input is not an integer


# Function to find Progression Outcome
def get_progression_outcome(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits  # Calculate the total credits

    if total_credits != TOTAL_CREDITS:  # Check if the total credits is 120
        return "Total incorrect"

    if pass_credits == PASS_CREDITS[0]:  # Check if the pass credits is 120
        return "Progress"
    elif pass_credits == PASS_CREDITS[1]:  # Check if the pass credits is 100
        return "Progress (module trailer)"
    elif fail_credits >= PASS_CREDITS[2]:  # Check if the fail credits is greater than or equal to 80
        return "Exclude"
    else:  # If none of the above conditions are true
        return "Do not progress – module retriever"


# Function to draw histogram
"""
    reference: https://www.w3schools.com/python/python_try_except.asp
    https://www.youtube.com/watch?v=R39vTAj1u_8
    https://www.youtube.com/watch?v=qVd9WRMuVRc&list=PL5FKO8x2yHG-UM-6otrJ0aqyg_wWsfb0B
"""


def draw_histogram(scaled_data, original_data):  # data_spaces is data with scaled values and data is original data
    try:
        win = GraphWin("Histogram", 600, 400)  # Create a window
        win.setCoords(0, -3, 10, 15)  # Set window coordinates

        # Draw a title
        title = Text(Point(2.4, 13.5), "Histogram Results")  # Create the title
        title.setFill(color_rgb(101, 101, 101))  # Set title color
        title.setSize(15)  # Set title size
        title.setStyle("bold")  # Set the style of the title
        title.draw(win)  # Draw the title

        # Draw a line
        base_line = Line(Point(0.5, 0), Point(9.5, 0))  # Create a line
        base_line.setWidth(0.5)  # Set line width
        base_line.draw(win)  # Draw the line

        # Draw "Progress" bar
        progress_bar = Rectangle(Point(1, 0), Point(2.895, scaled_data["Progress"]))  # Create rectangle
        progress_bar.setFill(color_rgb(174, 248, 161))  # Set a color
        progress_bar.draw(win)  # Draw that created rectangle

        progress_label = Text(Point(1.9475, scaled_data["Progress"] + 1),
                              str(original_data["Progress"]))  # Create a label
        progress_label.draw(win)  # Draw that label
        progress_text = Text(Point(1.9475, -0.6), "Progress")  # Create a bar title
        progress_text.setFill(color_rgb(101, 101, 101))  # Set color for the bar title
        progress_text.setStyle("bold")  # Bold the bar title
        progress_text.draw(win)  # Draw the bar title

        # Draw "Trailer" bar
        trailer_bar = Rectangle(Point(3.035, 0), Point(4.93, scaled_data["Trailer"]))  # Create a rectangle
        trailer_bar.setFill(color_rgb(160, 198, 137))  # Set a color
        trailer_bar.draw(win)  # Draw that created rectangle

        trailer_label = Text(Point(3.9825, scaled_data["Trailer"] + 1), str(original_data["Trailer"]))  # Create a label
        trailer_label.draw(win)  # Draw that label
        trailer_text = Text(Point(3.9825, -0.6), "Trailer")  # Create a bar title
        trailer_text.setFill(color_rgb(101, 101, 101))  # Set color for the bar title
        trailer_text.setStyle("bold")  # Bold the bar title
        trailer_text.draw(win)  # Draw the bar title

        # Draw "Retriever" bar
        retriever_bar = Rectangle(Point(5.07, 0), Point(6.965, scaled_data["Retriever"]))  # Create a rectangle
        retriever_bar.setFill(color_rgb(167, 188, 119))  # Set a color
        retriever_bar.draw(win)  # Draw that created rectangle

        retriever_label = Text(Point(6.0175, scaled_data["Retriever"] + 1),
                               str(original_data["Retriever"]))  # Create a label
        retriever_label.draw(win)  # Draw that label
        retriever_text = Text(Point(6.0175, -0.6), "Retriever")  # Create a bar title
        retriever_text.setFill(color_rgb(101, 101, 101))  # Set color for the bar title
        retriever_text.setStyle("bold")  # Bold the bar title
        retriever_text.draw(win)  # Draw the bar title

        # Draw the "Exclude" bar
        exclude_bar = Rectangle(Point(7.105, 0), Point(9, scaled_data["Exclude"]))  # Create a rectangle
        exclude_bar.setFill(color_rgb(210, 182, 181))  # Set a color
        exclude_bar.draw(win)  # Draw that created rectangle

        exclude_label = Text(Point(8.0525, scaled_data["Exclude"] + 1), str(original_data["Exclude"]))  # Create a label
        exclude_label.draw(win)  # Draw that label
        exclude_text = Text(Point(8.0525, -0.6), "Exclude")  # Create a bar title
        exclude_text.setFill(color_rgb(101, 101, 101))  # Set color for the bar title
        exclude_text.setStyle("bold")  # Bold the bar title
        exclude_text.draw(win)  # Draw the bar title

        total_label = Text(Point(2.9, -1.8),
                           f"{sum(original_data.values())} outcomes in total.")  # Create a label with total number of outcomes
        total_label.setFill(color_rgb(101, 101, 101))  # Set color for the label
        total_label.setStyle("bold")  # Bold the label
        total_label.setSize(14)  # Set size for the label
        total_label.draw(win)  # Draw the label

        win.getMouse()  # Wait for a mouse click
        win.close()  # Close the window

    except GraphicsError:  # Print an error if an error occurred during graphics operations
        print("An error occurred during graphics operations.")


# Function to save data to a file
"""
    reference: https://www.w3schools.com/python/python_file_write.asp
"""


def save_data_to_file(data):
    with open("progression_data.txt", "w") as file:  # Open the file
        for outcome, pass_credits, defer_credits, fail_credits in data:  # Write data to the file
            file.write(f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}\n")  # Write data to the file


# Function to print data from a file
"""
    reference: https://www.w3schools.com/python/ref_string_strip.asp#:~:text=The%20strip()%20method%20removes,any%20whitespaces%20will%20be%20removed
"""


def print_data_from_file():
    try:
        with open("progression_data.txt", "r") as file:  # Open the file
            print("Part 3:")
            for line in file:  # Print data from the file
                print(line.strip())
    except FileNotFoundError:
        print("No progression data found.")


# Function is to get user input and calculate progression outcome for a student user
def student_user():
    while True:  # Loop until the input is valid
        try:
            pass_credits = validate_input(input("Enter your total PASS credits: "), PASS_CREDITS)  # Validate the input
            if pass_credits is None:  # If input is not valid - continue the loop
                continue

            defer_credits = validate_input(input("Enter your total DEFER credits: "),
                                           PASS_CREDITS)  # Validate the input
            if defer_credits is None:  # If input is not valid - continue the loop
                continue

            fail_credits = validate_input(input("Enter your total FAIL credits: "), PASS_CREDITS)  # Validate the input
            if fail_credits is None:  # If input is not valid - continue the loop
                continue

            outcome = get_progression_outcome(pass_credits, defer_credits,
                                              fail_credits)  # Get progression outcome for the user's inputs
            print(outcome)  # Print the outcome
            break  # Break the loop

        except ValueError:  # If the input is not an integer
            print("Integer required.")  # Print an error message
            continue


# Main function to run program and get progression outcome
def main():
    user_type = input("Are you a student (s) or staff (st)? \nor Enter another input for quit : ").lower()  # Get user type

    if user_type == "s":  # If user type is student
        student_user()  # Call student_user function
        input("Press enter to Quit.")  # Wait for user to press enter
        quit()  # Quit the program

    elif user_type == "st":  # If user type is staff
        data = []  # Create a list to store data

        while True:  # Loop until user wants to quit
            try:
                pass_credits = validate_input(input("Enter your total PASS credits: "), PASS_CREDITS)  # Validate input
                if pass_credits is None:  # If input is not valid - continue the loop
                    continue

                defer_credits = validate_input(input("Enter your total DEFER credits: "),
                                               PASS_CREDITS)  # Validate input
                if defer_credits is None:  # If input is not valid - continue the loop
                    continue

                fail_credits = validate_input(input("Enter your total FAIL credits: "), PASS_CREDITS)  # Validate input
                if fail_credits is None:  # If input is not valid - continue the loop
                    continue

                outcome = get_progression_outcome(pass_credits, defer_credits,
                                                  fail_credits)  # Get progression outcome for the user's inputs
                print(outcome)  # Print the outcome

                data.append((outcome, pass_credits, defer_credits, fail_credits))  # Save the data to the list

                while True:  # Loop until the input is valid
                    choice = input(
                        "Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")  # Get user choice
                    if choice not in ['y', 'q']:  # If input is not valid - continue the loop
                        print("Wrong input")  # Print an error message
                        continue
                    break  # Break the loop
                if choice == 'q':  # If user wants to quit
                    histogram_data = {"Progress": 0, "Trailer": 0, "Retriever": 0,
                                      "Exclude": 0}  # Create a dictionary to store original data for histogram
                    scaled_histogram_data = {"Progress": 0, "Trailer": 0, "Retriever": 0,
                                             "Exclude": 0}  # Create a dictionary to store scaled data for histogram

                    for outcome, _, _, _ in data:  # Count the number of each outcome
                        if outcome == "Progress":  # If outcome is "Progress"
                            histogram_data["Progress"] += 1  # Increment the number of "Progress" outcomes
                        elif outcome == "Progress (module trailer)":  # If outcome is "Progress (module trailer)"
                            histogram_data["Trailer"] += 1  # Increment the number of "Trailer" outcomes
                        elif outcome == "Do not progress – module retriever":  # If outcome is "Do not progress – module retriever"
                            histogram_data["Retriever"] += 1  # Increment the number of "Retriever" outcomes
                        else:  # If outcome is "Exclude"
                            histogram_data["Exclude"] += 1  # Increment the number of "Exclude" outcomes

                    max_value = max(histogram_data.values())  # Find the maximum value in the histogram data

                    if max_value > 11:  # If the maximum value is greater than 11, scale all values
                        scale_factor = max_value / 11  # Calculate the scale factor
                        for key in histogram_data:  # Scale all values
                            scaled_histogram_data[key] = histogram_data[key] / scale_factor
                    else:  # If the maximum value is less than or equal to 11, do not scale
                        for key in histogram_data:  # Do not scale
                            scaled_histogram_data[key] = histogram_data[
                                key]  # Set the scaled value same as the original value

                    draw_histogram(scaled_histogram_data,
                                   histogram_data)  # Draw histogram with scaled data and original data

                    print("Part 2:")
                    for outcome, pass_credits, defer_credits, fail_credits in data:  # Print data from the list
                        print(f"{outcome} - {pass_credits}, {defer_credits}, {fail_credits}")

                    save_data_to_file(data)  # Save data to a file
                    print_data_from_file()  # Print data from a file
                    break  # Break the loop

                else:
                    continue

            except ValueError:  # If the input is not an integer
                print("Integer required.")
                continue

    else: # If user type is not student or staff
        print("Thank You!")
        quit() # Quit the program


if __name__ == "__main__":  # Run the program
    main()  # Call main function
