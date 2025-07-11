from flask import Flask, render_template, request, jsonify
import pyttsx3

app = Flask(__name__)
engine = pyttsx3.init()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    user_input = data.get('text', '')

    # Sample logic
    if "hello" in user_input.lower():
        response = "Hi there! How can I help you today?"
    elif "time" in user_input.lower():
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        response = f"The current time is {now}."
    else:
        response = "Sorry, I didn't understand that."

    # Text to speech response
    engine.say(response)
    engine.runAndWait()

    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True)
