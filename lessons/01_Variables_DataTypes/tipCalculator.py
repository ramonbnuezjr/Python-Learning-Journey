user_tip = float(input("What is the total bill amount? "))
tip_percentage = float(input("What is the tip percentage you would like to leave? "))

tip_amount = (user_tip) * (tip_percentage) / 100

print(f"Based on a bill amount of ${user_tip:.2f} and a tip percentage of {tip_percentage:.1f}%, you should leave a tip of ${tip_amount:.2f}.")