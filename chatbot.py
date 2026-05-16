import os
from openai import OpenAI

class AIChatbot:
    def __init__(self, api_key, memory_limit=5):
        
        # Initialise with OpenAI API and create a memory limit to store past conversations to save on tokens and lower latency required for competitive gaming.
        self.client = OpenAI(api_key=api_key)
        self.memory_limit = memory_limit
        
        # Create the personality for the chatbot.
        self.bot_personality = {
            "role": "system",
            "content": (
                "You are an encouraging and optimistic AI gaming companion."
                "Your goal is to provide meaningful and supportive feedback. "
                "Speak optimistically and use gaming terminology. "
                "Keep responses under 3 sentences."
            )
        }
        
        # Store the bot personality as the first item in the conversations that occurs.
        self.chat_history = [self.bot_personality]

    def chat(self, user_input):
        
        # Implement the conversation process and manage the chat history.

        # User writes a prompt. Add prompt to chat history.
        self.chat_history.append({"role": "user", "content": user_input})

        # Call the OpenAI API, using gpt-4o-mini for lower latency
        try:
            response = self.client.chat.completions.create(
                model = "gpt-4o-mini",
                messages = self.chat_history,
                temperature = 0.7 # To be adjusted based on desired creativity.
            )
            bot_reply = response.choices[0].message.content
        
        except Exception as e:
            return f"Error in API call.({e})"

        # Append bot reply to chat history.
        self.chat_history.append({"role": "assistant", "content": bot_reply})

        # Manage chat history to keep it small to save on tokens and reduce latency.
        # Bot personality is first item, then we keep the most recent conversations up to twice the memory limit as each chat consists of user prompt and bot reply.
        if len(self.chat_history) > (self.memory_limit * 2) + 1:
            self.chat_history = [self.chat_history[0]] + self.chat_history[-(self.memory_limit * 2):]

        return bot_reply

# Chatbot loop

if __name__ == "__main__":
    # Get key in the system environment
    api_key = os.getenv("OPENAI_API_KEY") 
    
    # Otherwise paste the key to run (if you dont't want to set up api key as environment variable)
    if not api_key:
        print("Warning: OPENAI_API_KEY environment variable not found.")
        api_key = input("Enter OpenAI API key to run the chatbot: ")
        
        # If they just hit enter without pasting anything, exit.
        if not api_key.strip():
            print("ERROR: API KEY REQUIRED. EXITING PROGRAM.")
            exit()

    print("\nStarting chatbot (Type 'quit' to exit)")
    print("-" * 50)
    
    # Run the chatbot loop.
    bot = AIChatbot(api_key=api_key, memory_limit=4)

    while True:
        user_text = input("Player: ")
        if user_text.lower() == "quit":
            print("Exiting chatbot.")
            break
            
        reply = bot.chat(user_text)
        print(f"Companion: {reply}\n")