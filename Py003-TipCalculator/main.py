# Welcome message
print("Welcome to Tip Calculator!")

# Get bill amount, tip percentage, and number of people
totalBill = float(input("Enter the amount of bill:\n"))
totalTip = int(input("How much tip would you like to leave? (10, 12, 15):\n"))
totalPeople = int(input("Among how many people is the bill to be divided into?:\n"))

# Calculate the tip and split the bill
finalTip = totalBill * (totalTip / 100)
finalBill = (totalBill + finalTip) / totalPeople

# Display the amount each person should pay
print(f"Your bill per person is ${finalBill:.2f}")
