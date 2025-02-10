user_name = input("What is your name? ")
user_age = int(input("How old are you? "))
user_height =float(input("How tall are you? "))
user_favorite_number = int(input("What is your favorite number? ")) * 2

while True: # This creates an infinite loop that will keep running until the user provides a valid response.
    user_student = input("Are you a student (yes or no)? ")
    if user_student.lower() == "yes" or user_student.lower() == "no":
        break # Exit the loop if the user provides a valid response.
    else:
        print("Please enter a valid response.")
        continue # Skip the rest of the loop and prompt the user again.
 
print(f"Hello {user_name}, you are {user_age} years old, {user_height:.1f} meters tall, and you are {'a student' if user_student.lower() == 'yes' else 'not a student'}.")