"""
Simple Rule-Based Chatbot
--------------------------
Responds to predefined user inputs using if-else logic.
Runs continuously until the user types an exit command.
"""

def get_response(user_input):
    """Return a canned response based on simple keyword matching."""
    text = user_input.lower().strip()

    # Greetings
    if text in ("hi", "hello", "hey", "hola"):
        return "Hello there! How can I help you today?"

    elif text in ("how are you", "how are you?", "how's it going"):
        return "I'm just a program, but I'm running smoothly. Thanks for asking!"

    elif "name" in text:
        return "I'm a simple rule-based chatbot. You can call me ChatBot."

    elif text in ("help", "what can you do"):
        return "I can greet you, chat a little, and say goodbye. Try saying 'hi' or 'bye'!"

    elif text in ("thanks", "thank you"):
        return "You're welcome!"

    elif text == "":
        return "Did you mean to say something? I'm listening."

    else:
        return "Sorry, I don't understand that yet. Try 'help' to see what I can do."


def main():
    print("ChatBot: Hello! Type 'bye', 'exit', or 'quit' to end our chat.\n")

    while True:
        user_input = input("You: ")

        # Exit commands
        if user_input.lower().strip() in ("bye", "exit", "quit"):
            print("ChatBot: Goodbye! Have a great day!")
            break

        response = get_response(user_input)
        print(f"ChatBot: {response}")


if __name__ == "__main__":
    main()


