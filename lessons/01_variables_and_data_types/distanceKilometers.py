# Write a program that asks the user for the distance in kilometers and then converts it to miles.
user_distance = float(input("What is the distance in kilometers? "))

# Convert the distance from kilometers to miles.
distance_miles = user_distance * 0.621371

# Print the result using formatted output.
print(f"The distance of {user_distance:.2f} kilometers is equal to {distance_miles:.2f} miles.")  # Use :.2f formatting to ensure two decimal places for readability.