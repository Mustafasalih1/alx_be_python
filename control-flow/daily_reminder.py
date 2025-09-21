task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

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