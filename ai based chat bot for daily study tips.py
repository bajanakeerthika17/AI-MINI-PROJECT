import random
import datetime

# List of daily study tips
study_tips = [
    "Take short breaks every 45 minutes to boost concentration.",
    "Revise your notes after each class to strengthen memory.",
    "Use the Pomodoro technique — study 25 mins, rest 5 mins.",
    "Stay hydrated! Your brain works better when you drink water.",
    "Teach someone else what you just learned — it helps retention.",
    "Avoid multitasking. Focus on one topic at a time.",
    "Set small, achievable goals for each study session.",
    "Sleep at least 7 hours to keep your mind sharp.",
    "Use active recall instead of just re-reading notes.",
    "Keep your phone away while studying to avoid distractions."
]

# Simple responses for user inputs
responses = {
    "hello": "Hey there! Ready to get a new study tip?",
    "hi": "Hi! Let’s make studying more fun today!",
    "thanks": "You’re welcome! Keep learning! 📚",
    "bye": "Goodbye! Stay consistent with your studies. 👋"
}

def get_daily_tip():
    """Return a random study tip."""
    return random.choice(study_tips)

def chatbot():
    print("🤖 AI StudyBot: Hello! I’m your Study Assistant.")
    print("Type 'tip' for a study tip or 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").lower().strip()

        if "bye" in user_input:
            print("AI StudyBot:", responses["bye"])
            break

        elif "tip" in user_input:
            today = datetime.datetime.now().strftime("%A, %d %B %Y")
            print(f"AI StudyBot: ({today}) {get_daily_tip()}")

        elif user_input in responses:
            print("AI StudyBot:", responses[user_input])

        elif user_input == "":
            print("AI StudyBot: Please type something 🙂")

        else:
            print("AI StudyBot: I can share study tips! Try typing 'tip' or 'hello'.")

# Run chatbot
if __name__ == "__main__":
    chatbot()
