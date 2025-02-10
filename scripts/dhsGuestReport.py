import pandas as pd
import matplotlib.pyplot as plt

# Load CVS file.
data = pd.read_csv('data/dhsGuest.csv')

# Inspect the data.
# print(data.head())          # Display the first five rows of the data.
# print(data.columns)         # Display the column names of the data.

# Filter the data.
data = data[data["ExternalUserState"]== "PendingAcceptance"]

# Get the unique values of the column.
count = data.shape[0]

# Print the count.
print(f"Pending Acceptence is: {count}")

# Count occurrences of each user state
state_counts = data["ExternalUserState"].value_counts()

# Plot a bar chart
state_counts.plot(kind='bar')
plt.title("User States Count")
plt.xlabel("External User State")
plt.ylabel("Number of Users")
plt.xticks(rotation=45)  # Rotate labels for better readability
plt.show()