task = input("Enter your priority task for today: ")
priority = input("Enter task priority (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()
    
print("\n--- Your Reminder ---")
    
match priority:
    case "high":
        urgency = "URGENT"
    case "medium":
        urgency = "Important"
    case "low":
        urgency = "When you have time"
    case _:
        urgency = "Unknown priority"
    
time_sensitive = "that requires immediate attention today!" if time_bound == "yes" else "to complete today."
    
print(f"\n{urgency.upper()} TASK: {task} {time_sensitive}")

if priority == "high" and time_bound == "yes":
    print("\nReminder: 'Finish {urgency}' is a high priority task that requires immediate attention today!")
elif priority == "low":
    print("\nNote: '{urgency}' is a low priority task. Consider completing it when you have free time.")
