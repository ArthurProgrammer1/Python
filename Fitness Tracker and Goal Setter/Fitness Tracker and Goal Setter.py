import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

file_name = "fitness_data.csv"
if os.path.exists(file_name):
    df = pd.read_csv(file_name)
else:
    df = pd.DataFrame(columns=["Date", "Exercise", "Duration (mins)", "Calories Burned"])

def add_activity(date, exercise, duration, calories):
    """
    Adds a new fitness activity to the DataFrame and saves it to a CSV file.
    """
    global df
    new_row = pd.DataFrame([[date, exercise, duration, calories]], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(file_name, index=False)
    print("Activity added successfully!")

def view_progress():
    """
    Plots the user's progress over time for exercise duration and calories burned.
    """
    global df
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by='Date', inplace=True)

    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(df['Date'], df['Duration (mins)'], marker='o', linestyle='-')
    plt.title('Exercise Duration Over Time')
    plt.xlabel('Date')
    plt.ylabel('Duration (mins)')
    
    plt.subplot(1, 2, 2)
    plt.plot(df['Date'], df['Calories Burned'], marker='o', linestyle='-', color='orange')
    plt.title('Calories Burned Over Time')
    plt.xlabel('Date')
    plt.ylabel('Calories Burned')
    
    plt.tight_layout()
    plt.show()

def set_goal(goal_type, target_value, period):
    """
    Sets a goal for the user to achieve within a certain period.
    
    Parameters:
    - goal_type (str): The type of goal ('Duration' or 'Calories').
    - target_value (float): The target value to achieve.
    - period (str): The period for the goal ('daily', 'weekly', 'monthly').
    """
    print(f"Goal set! Aim to achieve {target_value} {goal_type.lower()} per {period}. Keep pushing your limits!")

def display_menu():
    """
    Displays the menu for user interaction.
    """
    print("\nFitness Tracker Menu:")
    print("1. Add a new activity")
    print("2. View progress")
    print("3. Set a fitness goal")
    print("4. Exit")

def main():
    """
    Main function to run the fitness tracker application.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            exercise = input("Enter the exercise (e.g., Running, Cycling): ")
            try:
                duration = float(input("Enter the duration (minutes): "))
                calories = float(input("Enter the calories burned: "))
                add_activity(date, exercise, duration, calories)
            except ValueError:
                print("Invalid input. Please enter numeric values for duration and calories.")
        
        elif choice == '2':
            view_progress()
        
        elif choice == '3':
            goal_type = input("Enter the goal type ('Duration' or 'Calories'): ")
            try:
                target_value = float(input("Enter the target value: "))
                period = input("Enter the period ('daily', 'weekly', 'monthly'): ")
                set_goal(goal_type, target_value, period)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the target.")
        
        elif choice == '4':
            print("Exiting the fitness tracker. Stay healthy!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
