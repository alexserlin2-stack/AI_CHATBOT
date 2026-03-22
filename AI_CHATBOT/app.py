from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Basic chatbot logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great! How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I don't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    bot_reply = get_bot_response(user_input)
    return jsonify({"bot_reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)