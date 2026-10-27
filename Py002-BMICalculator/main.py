# Welcome message
print("Welcome to BMI Calculator!")

# Get weight and height from the user
userWeight = float(input("Enter your weight (in kgs.):\n"))
userHeight = float(input("Enter your height (in meters):\n"))

# Calculate and display BMI
userBMI = userWeight / (userHeight ** 2)
print(f"Your BMI is {userBMI:.2f}!")

# Display BMI category
if userBMI < 18.5:
    print("You are underweight!")
elif userBMI > 25:
    print("You are overweight!")
else:
    print("You are in the normal weight range!")
