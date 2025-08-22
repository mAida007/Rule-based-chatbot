# chatbot.py

faq_data = {
    "services": "We offer mobile, web, and desktop application development services.",
    "mobile app cost": "The cost of a mobile app varies based on features, typically ranging from $500 to $5000.",
    "getting started": "You can get started by contacting us with your idea and requirements.",
    "contact": "You can contact us via email at contact@company.com.",
    "technologies": "We work with Python, React, Node.js, Flutter, and more.",
    "timeline": "Project timelines depend on scope, usually between 2 weeks to 3 months.",
    "platforms": "We develop for Android, iOS, Windows, and Web platforms."
}

clarification_questions = [
    "Do you need a mobile, web, or desktop solution?",
    "Can you tell me more about your business type?"
]

greetings = ["hi", "hello", "hey"]
thanks = ["thank you", "thanks"]

def get_response(user_input):
    user_input = user_input.lower()
    if user_input in greetings:
        return "Hello! How can I help you today?"
    elif user_input in thanks:
        return "You're welcome! Let me know if you have more questions."
    else:
        for keyword, answer in faq_data.items():
            if keyword in user_input:
                return answer
        for q in clarification_questions:
            if any(w in user_input for w in ["solution", "business"]):
                return q
        return "Sorry, I didn’t understand that. Can you rephrase it?"

def main():
    print("Welcome to the Software Services FAQ Bot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot: Thank you for visiting! Have a great day.")
            break
        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
