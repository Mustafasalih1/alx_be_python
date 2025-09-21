task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        print(f"Reminder: '{task}' is a low priority task.")
    case _:
        print(f"Reminder: '{task}' has an unknown priority.")

if time_bound == "yes":
    print("This task requires immediate attention today!")
elif time_bound == "no":
    print(" Consider completing it when you have free time.")