# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Takes a score (0-100) and returns the letter grade.
# A = 70+, B = 60-69, C = 50-59, D = 40-49, F = below 40

def calculate_grade(score):
    # TODO: implement grade logic
    pass
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"
score = int(input("Enter your score (0-100): "))
grade = calculate_grade(score)
print("Your grade is:", grade)

# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.

def multiplication_table():
    # TODO: implement loop and table logic
    pass
    while True:
        number = input("Enter a number (or 'quit' to exit): ")

        if number.lower() == "quit":
            print("Goodbye!")
            break

        number = int(number)

        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")


multiplication_table()

# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().

def your_function():
    # TODO: implement your chosen function
    pass
# Function 3: Currency Converter
# Converts Nigerian Naira to US Dollars.

def convert_currency():
    naira = float(input("Enter amount in Naira: "))
    exchange_rate = float(input("Enter exchange rate (NGN per USD): "))

    dollars = naira / exchange_rate

    print("Amount in Naira: ₦", naira)
    print("Amount in Dollars: $", round(dollars, 2))


convert_currency()

# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    # TODO: build the menu here
    pass
# Main Menu
# Allows the user to choose which function to run.

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Currency Converter")
        print("4. Exit")

        try:
            choice = int(input("Choose an option (1-4): "))

            if choice == 1:
                calculate_grade()

            elif choice == 2:
                multiplication_table()

            elif choice == 3:
                convert_currency()

            elif choice == 4:
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
