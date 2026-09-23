from flask import Flask, request, jsonify
from flask_cors import CORS

import datetime
import random
import re


app = Flask(__name__)

CORS(app)


# ---------------------------------------------------------
# Professional Rule-Based Chatbot
# ---------------------------------------------------------

class ProfessionalChatbot:

    def __init__(self):

        self.name = None

        self.responses = {

            "greeting": [
                "Hello! 👋 It's great to meet you. How can I help you today?",
                "Hi there! 😊 What can I do for you?",
                "Hey! 👋 I'm here to help. What's on your mind?"
            ],

            "how_are_you": [
                "I'm doing great! Thanks for asking. 😊 How are you?",
                "I'm working perfectly and ready to help you!",
                "I'm doing well! What would you like to talk about?"
            ],

            "thanks": [
                "You're very welcome! 😊",
                "My pleasure! I'm always happy to help.",
                "You're welcome! Let me know if you need anything else."
            ],

            "goodbye": [
                "Goodbye! 👋 Have a wonderful day!",
                "See you later! Take care. 😊",
                "It was nice talking with you. Goodbye!"
            ],

            "compliment": [
                "Thank you so much! 😊 I really appreciate that.",
                "That's very kind of you! I'm glad I could help.",
                "Thanks! Your feedback means a lot."
            ]
        }


    # -----------------------------------------------------
    # Main Response Function
    # -----------------------------------------------------

    def get_response(self, user_input):

        text = user_input.lower().strip()


        # Empty input
        if not text:

            return "Please type something so I can help you. 😊"


        # Exit commands
        if re.search(
            r"\b(bye|goodbye|exit|quit|see you)\b",
            text
        ):

            return random.choice(
                self.responses["goodbye"]
            )


        # Greeting
        if re.search(
            r"\b(hi|hello|hey|hii|helo|good morning|good afternoon|good evening)\b",
            text
        ):

            return random.choice(
                self.responses["greeting"]
            )


        # Name introduction
        name_match = re.search(
            r"(my name is|i am|i'm|call me)\s+([a-zA-Z]+)",
            text
        )


        if name_match:

            self.name = name_match.group(2).capitalize()

            return (
                f"Nice to meet you, {self.name}! 😊 "
                "How can I help you today?"
            )


        # Asking chatbot's name
        if (
            "your name" in text
            or "who are you" in text
            or "what are you" in text
        ):

            return (
                "I'm a professional rule-based chatbot created "
                "using Python. I understand common user queries "
                "and respond using predefined rules."
            )


        # How are you
        if (
            "how are you" in text
            or "how r u" in text
            or "how are u" in text
        ):

            return random.choice(
                self.responses["how_are_you"]
            )


        # User's name
        if (
            "my name" in text
            or "do you know my name" in text
        ):

            if self.name:

                return f"Your name is {self.name}. 😊"

            else:

                return (
                    "I don't know your name yet. "
                    "You can tell me by saying: "
                    "My name is Divyansh."
                )


        # Help
        if (
            "help" in text
            or "what can you do" in text
            or "how can you help" in text
        ):

            return (
                "I can help with several common conversations:<br><br>"
                "• Greetings<br>"
                "• Your name<br>"
                "• Date and time<br>"
                "• Basic information<br>"
                "• Python-related questions<br>"
                "• Internship/project questions<br>"
                "• General conversation<br><br>"
                "Just type your question naturally."
            )


        # Time
        if (
            "time" in text
            or "current time" in text
            or "what time is it" in text
        ):

            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            return f"The current time is {current_time}. ⏰"


        # Date
        if (
            "date" in text
            or "today" in text
            or "what day is it" in text
        ):

            current_date = datetime.datetime.now().strftime(
                "%A, %d %B %Y"
            )

            return f"Today is {current_date}. 📅"


        # Python questions
        if "python" in text:

            if (
                "what is python" in text
                or text == "python"
            ):

                return (
                    "Python is a high-level, interpreted "
                    "programming language known for its simple "
                    "syntax and wide range of applications "
                    "including web development, automation, "
                    "data science and AI."
                )


            if (
                "learn python" in text
                or "learn python?" in text
            ):

                return (
                    "A good way to learn Python is to start with:<br><br>"
                    "1. Variables and data types<br>"
                    "2. Conditions and loops<br>"
                    "3. Functions<br>"
                    "4. Lists, tuples and dictionaries<br>"
                    "5. Object-oriented programming<br>"
                    "6. Projects and problem solving"
                )


            if (
                "python used for" in text
                or "uses of python" in text
            ):

                return (
                    "Python is commonly used for Web Development, "
                    "Artificial Intelligence, Machine Learning, "
                    "Data Science, Automation and Software Development."
                )


        # AI questions
        if (
            "artificial intelligence" in text
            or text == "ai"
            or "what is ai" in text
            or "define ai" in text
        ):

            return (
                "Artificial Intelligence (AI) is a field of "
                "computer science that focuses on creating "
                "systems capable of performing tasks that "
                "normally require human intelligence, such as "
                "learning, reasoning and problem solving."
            )


        # Internship
        if "internship" in text:

            return (
                "An internship gives you practical experience "
                "by allowing you to work on real-world projects. "
                "It can also help improve your skills, resume "
                "and professional portfolio."
            )


        # Projects
        if (
            "project" in text
            or "projects" in text
        ):

            return (
                "Projects are one of the best ways to demonstrate "
                "your skills. For an AI internship, projects such "
                "as chatbots, recommendation systems and computer "
                "vision applications can be useful."
            )


        # Thanks
        if re.search(
            r"\b(thanks|thank you|thankyou|thx|ty)\b",
            text
        ):

            return random.choice(
                self.responses["thanks"]
            )


        # Compliments
        if re.search(
            r"\b(good bot|nice bot|great bot|awesome|good job|well done)\b",
            text
        ):

            return random.choice(
                self.responses["compliment"]
            )


        # Simple questions
        if text.endswith("?"):

            return (
                "That's an interesting question! 🤔<br><br>"
                "I'm currently a rule-based chatbot, so I can "
                "answer questions that are covered by my "
                "predefined knowledge and rules.<br><br>"
                "Try asking me about Python, AI, internships, "
                "projects, date, time, or say 'help' to see "
                "what I can do."
            )


        # Default response
        return (
            "I understand what you're saying. 😊<br><br>"
            "However, I don't have a predefined response for "
            "that yet. Try asking me something related to "
            "Python, AI, projects, internships, date, time, "
            "or type 'help'."
        )


# Create chatbot object
chatbot = ProfessionalChatbot()


# ---------------------------------------------------------
# API Route
# ---------------------------------------------------------

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    response = chatbot.get_response(user_message)

    return jsonify({
        "response": response
    })


# ---------------------------------------------------------
# Run Server
# ---------------------------------------------------------

if __name__ == "__main__":

    print("==============================================")
    print("       CODSOFT TASK 1 - AI CHATBOT")
    print("==============================================")
    print("Server running at:")
    print("http://127.0.0.1:5000")
    print("Keep this terminal running.")
    print("==============================================")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )