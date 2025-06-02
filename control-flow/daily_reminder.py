task = str(input("Enter your task:"))
priority = str (input("Priority (high/medium/low):"))
time_bound = str(input("Is it time-bound? (yes/no):"))

match priority:
    case "high":
        message = f"Reminder: {task} is a high priority task."
    case "medium":
        message = f"Reminder: {task} is a medium priority task."
    case "low":
        message = f"Reminder: {task} is a low priority task."
    case _:
        message = f"Reminder: {task} is unknown priority"

if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no":
    message += " Consider completing it when you have free time."
print(f"Reminder: {message}")