def chatbot():
    print("=== Basic Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! How are you?")

        elif user == "hi":
            print("Bot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine. Thank you!")

        elif user == "your name":
            print("Bot: I'm a Basic Chatbot.")

        elif user == "help":
            print("Bot: You can say hello, hi, how are you, your name, or bye.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()

