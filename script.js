const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const typing = document.getElementById("typing");


// =====================================================
// ADD MESSAGE
// =====================================================

function addMessage(message, sender) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message");

    if (sender === "user") {

        messageDiv.classList.add("user-message");

        messageDiv.innerHTML = `
            <div class="avatar">👤</div>

            <div class="message-content">
                <div class="sender">You</div>

                <div class="bubble">
                    ${message}
                </div>
            </div>
        `;

    } else {

        messageDiv.innerHTML = `
            <div class="avatar">🤖</div>

            <div class="message-content">
                <div class="sender">AI Assistant</div>

                <div class="bubble">
                    ${message}
                </div>
            </div>
        `;
    }

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


// =====================================================
// SEND MESSAGE
// =====================================================

async function sendMessage() {

    const message = userInput.value.trim();

    if (message === "") {
        return;
    }


    // Show user's question
    addMessage(message, "user");


    // Clear input
    userInput.value = "";


    // Show typing animation
    typing.style.display = "flex";


    try {

        const response = await fetch(
            "http://127.0.0.1:5000/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );


        const data = await response.json();


        // Hide typing
        typing.style.display = "none";


        // Show chatbot answer
        addMessage(data.response, "bot");

    }

    catch (error) {

        typing.style.display = "none";

        addMessage(
            "⚠️ Unable to connect to the chatbot server. Please make sure app.py is running.",
            "bot"
        );

        console.error(error);
    }
}


// =====================================================
// QUICK QUESTION BUTTON
// =====================================================

function quickMessage(message) {

    // Put question inside input
    userInput.value = message;

    // Automatically send it
    sendMessage();
}


// =====================================================
// SEND BUTTON
// =====================================================

sendBtn.addEventListener("click", sendMessage);


// =====================================================
// ENTER KEY
// =====================================================

userInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});