# AI Chatbot - Rule Based
# Name: Benedict Sau
# Registration Number: [Your Reg No]

def chatbot():
    print("Hello! I am your Course Assistant Bot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        # Intent 1: Greetings
        if any(word in user_input for word in ["hi", "hello", "hey"]):
            print("Bot: Hello! Nice to meet you. How can I assist you today?")
        
        # Intent 2: Course Info
        elif "courses" in user_input or "offer" in user_input:
            print("Bot: We offer AI, Data Science, Python Programming, and Cybersecurity courses.")
        
        # Intent 3: AI Basics
        elif "ai" in user_input or "artificial intelligence" in user_input:
            print("Bot: AI stands for Artificial Intelligence. It enables machines to mimic human intelligence.")
        
        # Intent 4: University Info
        elif "university" in user_input or "location" in user_input:
            print("Bot: The university is located at [Your University Location].")
        
        # Intent 5: Farewell
        elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
            print("Bot: Goodbye! Have a great day!")
            break
        
        # Unknown Input
        else:
            print("Bot: I’m sorry, I didn’t understand that. Can you please rephrase?")

# Run chatbot
if __name__ == "__main__":
    chatbot()
