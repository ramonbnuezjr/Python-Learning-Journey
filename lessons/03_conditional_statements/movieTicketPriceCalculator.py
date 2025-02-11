# Building a movie ticket price calculator based on user's age.
user_age = int(input("Enter your age: "))

# Determining ticket price based on user's age. 
if user_age < 5:
    ticket_price = 0
elif user_age >= 5 and user_age <= 12:
        ticket_price = 10
elif user_age >= 13 and user_age <= 60:
        ticket_price = 15
else: 
    ticket_price = 12

# Printing the results of the ticket price.
print("The ticket price is : $" + str(ticket_price))