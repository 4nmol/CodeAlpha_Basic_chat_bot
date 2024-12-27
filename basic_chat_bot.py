# A very basic chat bot created using python programming language.
import random

# This is the function I have created to handle responses
def chatbot_response(user_input):
    user_input = user_input.lower()  # I am Converting input to lowercase for easier matching

    # Predefined responses Which will given by chat bot
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey, how can I help you?"],
        "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?", "I'm great! How are you?"],
        "bye": ["Goodbye!", "See you later!", "Bye, have a nice day!"],
        "help": ["How can I assist you?", "What do you need help with?", "I'm here to help!"],
        "name": ["I am Chat Bot created using python", "My name is chat bot", "Chat bot"],
        "languages": ["Python java html css and many more, please know if you have more questiosns", "C programing"],
        "evening": ["Hello! Good evening How can I help you.", "Good evening !", "GE How can I assist you."],
        "morning": ["Hello! Good morning", "GM how are you", "Very Good morning"],
        "afternoon": ["Good afternoon!", "I am user friendly chat bot", "How can I help you"],
        "name": ["Good night!Sweet Dreams","Have a nice night", "Good night"],
        "dinner": ["I am machine so I dont do that", "I am unable to do it becuase I am machine have you ?", "I am Chat bot!"],
        "breakfast": ["I am machine so I dont do that", "I am unable to do it becuase I am machine have you ?", "I am Chat bot!"],
        "lunch": ["I am machine so I dont do that", "I am unable to do it becuase I am machine have you ?", "I am Chat bot!!"],
        "ok": ["What Help Can I provide to you ?"]

    }

    # Default response if no pattern matches
    default_response = "Sorry, I didn't understand that. Can you try again?"

    # Iterate over predefined responses and check if the user input matches any
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return default_response  # Return the default response if no match is found

# Main loop to interact with the chatbot
if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break  # Exit the loop 
        
        response = chatbot_response(user_input)  # Get the chatbot's response
        print(f"Chatbot: {response}")
