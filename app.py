from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import csv
from datetime import datetime
from flask import send_file
import os
from chat import get_response



app=Flask(__name__)
CORS(app)

csv_file_path = "chat_transcript.csv"


@app.get("/")
def index_get():
    return render_template("base.html")



@app.route("/download_csv")
def download_csv():
    global file_downloaded
    csv_file_path = "chat_transcript.csv"
    response =  send_file(csv_file_path, as_attachment=True)
    file_downloaded = True
    return response

def is_csv_empty(file_path):
    return os.path.getsize(file_path) == 0



def save_to_csv(user_message, bot_response):
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open("chat_transcript.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if(is_csv_empty(csv_file_path)):
            writer.writerow(["Bot", "User", "Time"])
        writer.writerow([bot_response, user_message, timestamp])

@app.post("/predict")
def predict():
    user_message = request.get_json().get("message")
    bot_response = get_response(user_message)
    message = {"answer": bot_response}
    
    # Save user message and bot response to CSV file
    save_to_csv(user_message, bot_response)
    
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)