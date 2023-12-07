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

    # Insert sample data into landmarks table
    cursor.executemany('''
        INSERT INTO landmarks (name, description) VALUES (?, ?)
    ''', [
        ('Volcanoes National Park', 'Home to endangered mountain gorillas and stunning volcanic landscapes.'),
        ('Akagera National Park', 'A diverse wildlife park with savannah, lakes, and the Akagera River.'),
        ('Kigali Genocide Memorial', 'A memorial honoring the victims of the Rwandan Genocide.'),
        ('Lake Kivu', 'One of Africa\'s Great Lakes, known for its scenic beauty and resort towns.'),
        ('Nyungwe Forest National Park', 'A tropical rainforest with diverse flora, fauna, and chimpanzees.'),
        ('Inema Arts Center', 'An art space showcasing contemporary Rwandan and African art.')
    ])

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

# Function to display information about landmarks
def display_landmarks():
    # Connect to the database
    conn = sqlite3.connect("tourism_education.db")
    cursor = conn.cursor()

    # Fetch and display landmark information
    cursor.execute("SELECT * FROM landmarks")
    landmarks = cursor.fetchall()

    if landmarks:
        print("Here is information about the local landmarks:")
        for landmark in landmarks:
            print(f"ID: {landmark[0]}, Name: {landmark[1]}, Description: {landmark[2]}")
    else:
        print("No landmarks found in the database.")

    # Close the database connection
    conn.close()

# Function to display progress
def display_progress():
    # Connect to the database
    conn = sqlite3.connect("tourism_education.db")
    cursor = conn.cursor()

    # Fetch and display user progress
    cursor.execute("SELECT * FROM user_progress")
    user_progress = cursor.fetchall()

    if user_progress:
        print("Your progress:")
        for progress in user_progress:
            print(f"User ID: {progress[0]}, Landmarks Visited: {progress[1]}")
    else:
        print("No progress found in the database.")

    # Close the database connection
    conn.close()

# Function to mark a landmark as visited
def mark_visited_landmark():
    # Connect to the database
    conn = sqlite3.connect("tourism_education.db")
    cursor = conn.cursor()

    # Display the list of landmarks
    display_landmarks()

    # Get the landmark ID from the user
    landmark_id = input("Enter the ID of the landmark you have visited: ").strip()

    # Check if the landmark ID is valid
    cursor.execute("SELECT * FROM landmarks WHERE id = ?", (landmark_id,))
    landmark = cursor.fetchone()

    if landmark:
        # Fetch the current user progress
        user_id = 1  # Assuming a single user for simplicity
        cursor.execute("SELECT * FROM user_progress WHERE user_id = ?", (user_id,))
        user_progress = cursor.fetchone()

        # Update the user progress to include the visited landmark
        if user_progress:
            visited_landmarks = user_progress[1]
            if visited_landmarks:
                visited_landmarks += f", {landmark[1]}"
            else:
                visited_landmarks = landmark[1]

            cursor.execute("UPDATE user_progress SET landmarks_visited = ? WHERE user_id = ?", (visited_landmarks, user_id))
        else:
            cursor.execute("INSERT INTO user_progress (user_id, landmarks_visited) VALUES (?, ?)", (user_id, landmark[1]))

        print(f"You have successfully marked {landmark[1]} as visited!")
    else:
        print("Invalid landmark ID. Please try again.")

    # Commit changes and close the database connection
    conn.commit()
    conn.close()

# Function for chatting with the program
def chat_with_program():
    print("Chatting with the program... Ask me anything about tourism!")

# Main function to orchestrate the program
def main():
    create_database()  # Call create_database before main program execution
    welcome()

    while True:
        display_menu()
        choice = get_user_input("Enter the number of your choice (1-4): ", options=["1", "2", "3", "4"])

        if choice == "1":
            display_landmarks()
        elif choice == "2":
            chat_with_program()
        elif choice == "3":
            display_progress()
            mark_visited_landmark()
        elif choice == "4":
            print("Thank you for using the Tourism Education Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Execute the main function if the script is run
if __name__ == "__main__":
    main()
