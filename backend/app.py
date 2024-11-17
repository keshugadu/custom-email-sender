import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, request, jsonify
from email_sender import send_custom_email
from schedule_manager import schedule_email
from analytics_tracker import get_email_analytics
from data_loader import load_data_from_csv, load_data_from_google_sheet
from prompt_generator import generate_email_content

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    try:
        response = send_custom_email(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/schedule-email', methods=['POST'])
def schedule_email_route():
    data = request.json
    try:
        response = schedule_email(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/analytics', methods=['GET'])
def analytics():
    try:
        response = get_email_analytics()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    try:
        file = request.files['file']
        data = load_data_from_csv(file)
        return jsonify(data.to_dict(orient="records"))  # Convert data to JSON-serializable format
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/load-google-sheet', methods=['POST'])
def load_google_sheet():
    sheet_url = request.json.get('sheet_url')
    creds_file = 'path_to_creds.json'  # Make sure creds.json is in the root directory or provide the full path
    try:
        data = load_data_from_google_sheet(sheet_url, creds_file)
        return jsonify(data.to_dict(orient="records"))  # Convert to JSON-serializable format
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate-email-content', methods=['POST'])
def generate_email_content_route():
    data = request.json
    prompt_template = data.get('prompt_template')
    row_data = data.get('row_data')
    try:
        email_content = generate_email_content(prompt_template, row_data)
        return jsonify({"email_content": email_content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)