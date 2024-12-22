task = input("Enter your task: ")
priority = input("Priority (high/medium/low):")
time_variable = input("is the task time_bound? (yes/no): ")

match priority:
    case "high":
        if time_variable == "yes":
            print(
                f"Reminder: {task} is a {priority} priority task that requires immediate attention today!"
            )
        
        else:
            print(
                f"Note: {task} is a {priority} priority task. Consider completing it when you have free time."
            )

    case "medium":
        if time_variable == "yes":
            print(
                f"Reminder: {task} is a {priority} priority task that requires immediate attention today!"
            )
        else:
            print(
                f"Note: {task} is a {priority} priority task. Consider completing it when you have free time."
            )

    case "low":
        if time_variable == "yes":
            print(
                f"Reminder: {task} is a {priority} priority task that requires immediate attention today!"
            )
        else:
            print(
                f"Note: {task} is a {priority} priority task. Consider completing it when you have free time."
            )

    case _:
        print("Invalid priority level. Please enter high, medium, or low.")