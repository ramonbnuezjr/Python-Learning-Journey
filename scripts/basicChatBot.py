# Function to get non-blank input from the user.
def get_non_blank_input(prompt):
    response = input(prompt).strip()
    while not response:
        response = input("Please enter a valid response: ").strip()
    return response

# Description: A basic chatbot that asks the user how they are feeling today.

user_name = get_non_blank_input("What is your name?")  # Get user name.
user_feelings = get_non_blank_input("How are you feeling today?").lower()  # Get user input and convert to lower case.

if user_feelings == "happy":
    print(f"{user_name}, that's great to hear you are feeling happy!")
elif user_feelings == "sad":
    print(f"{user_name}, I'm sorry to hear you are feeling sad.")
elif user_feelings == "ok":
    print(f"{user_name}, I'm glad to hear that you are feeling OK")
else:
    print(f"I'm not sure how to respond to that, {user_name}, but I hope you have a great day!")