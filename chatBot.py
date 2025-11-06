# --- Function to get chatbot response ---
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 I'm Muskan's AI chatbot. How can I help you today?"

    # Asking about chatbot
    elif "who are you" in user_input:
        return "I'm a simple AI chatbot built using rule-based logic for my internship task."

    # Asking about creator
    elif "who created you" in user_input or "your creator" in user_input:
        return "I was created by Muskan Kumari as part of her Artificial Intelligence internship project."
 # Asking about feelings
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking! How about you?"

    # Help or guidance
    elif "help" in user_input:
        return "Sure! You can ask me about AI, internship tasks, or just chat casually 😊"

    # Questions about AI
    elif "what is ai" in user_input:
        return ("Artificial Intelligence (AI) is a branch of computer science "
                "that aims to create systems that can perform tasks that normally "
                "require human intelligence, like learning, reasoning, or problem-solving.")

    # About internship tasks
    elif "task" in user_input or "project" in user_input:
        return "There are three main tasks in this internship: Chatbot, Tic-Tac-Toe AI, and Image Captioning."

    # Goodbye
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! 👋 Have a great day ahead."

    # Default fallback response
    else:
        return "I'm not sure about that 🤔, but I’ll learn more soon!"

# --- Run the chatbot ---
print("🤖 Chatbot is ready! Type 'bye' to end the chat.\n")

while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Bot:", response)
    if "bye" in user.lower():
        break
