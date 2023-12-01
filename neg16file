#!/usr/bin/python3

import sqlite3

# Function to create the database and tables
def create_database():
    conn = sqlite3.connect("tourism_education.db")
    cursor = conn.cursor()

    # Create landmarks table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS landmarks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')

    # Create user progress table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_progress (
            user_id INTEGER PRIMARY KEY,
            landmarks_visited TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Function to welcome students to the program
def welcome():
    print("Welcome to the Tourism Education Program!")
    print("Let's explore the local tourism industry.\n")

# Function to display the main menu
def display_menu():
    print("MENU:")
    print("1. Learn about local landmarks and attractions")
    print("2. Chat with the program")
    print("3. View your progress")
    print("4. Exit")

# Function to handle user input and validation
def get_user_input(prompt, options=None):
    while True:
        user_input = input(prompt).strip()

        if options and user_input not in options:
            print("Invalid input. Please try again.")
        else:
            return user_input

# Main function to orchestrate the program
def main():
    create_database()
    welcome()

    while True:
        display_menu()
        choice = get_user_input("Enter the number of your choice (1-4): ", options=["1", "2", "3", "4"])

        if choice == "1":
            print("Explore local landmarks and attractions.")
        elif choice == "2":
            print("Chat with the program.")
        elif choice == "3":
            print("View your progress.")
        elif choice == "4":
            print("Thank you for using the Tourism Education Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Execute the main function if the script is run
if __name__ == "__main__":
    main()
