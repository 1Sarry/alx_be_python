task = str(input("Enter your task:"))
priority = str (input("Priority (high/medium/low):"))
time_bound = str(input("Is it time-bound? (yes/no):"))

match priority:
    case "high":
        reminder = f"Reminder: {task} is a high priority task."
    case "medium":
        reminder = f"Reminder: {task} is a medium priority task."
    case "low":
        reminder = f"Reminder: {task} is a low priority task."

if time_bound == "yes":
    reminder += " — that requires immediate attention today!"
print(reminder)