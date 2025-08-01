def chatbot():
    print("Welcome to the Basic Chatbot! Type something to start a conversation. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
