import datetime
from data_manager import add_activity, get_all_activities
from config import DB_PATH

def show_menu():
    print("\n--- Time Tracker ---")
    print("1. Add an activity")
    print("2. View summary")
    print("3. Improvement ideas")
    print("4. Exit")

def add_new_activity():
    activity_name = input("What did you do? ")
    hours_spent = float(input("How many hours did you spend on this activity? "))
    category = input("Category (e.g., Work, Leisure, etc.): ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    add_activity(activity_name, hours_spent, category, date)
    print(f"Activity '{activity_name}' added successfully!")

def view_summary():
    activities = get_all_activities()
    if activities:
        print("\n--- Summary of Activities ---")
        for activity in activities:
            print(f"Activity: {activity['name']}, Hours: {activity['hours']}, Category: {activity['category']}, Date: {activity['date']}")
    else:
        print("No activities recorded yet.")

def get_improvement_ideas():
    activities = get_all_activities()
    total_hours = sum([activity['hours'] for activity in activities])
    print(f"\nTotal hours spent: {total_hours}")
    
    wasted_time = total_hours - 8  # Assume 8 hours of productive time per day
    if wasted_time > 0:
        print(f"You've wasted {wasted_time} hours. Consider reducing non-productive time.")
    else:
        print("You're managing your time well!")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_new_activity()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            get_improvement_ideas()
        elif choice == "4":
            print("Exiting Time Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
