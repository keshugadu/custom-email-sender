CUSTOM EMAIL SENDER

Overview:

This is a Flask-based application designed for sending personalized emails. The application:
 -> Reads recipient data from Google Sheets or CSV files
 -> Uses OpenAI's API to generate custom email template based on user prompt
 -> Sends emails via SMTP (Eg.: Gmail, Outlook)
 -> Tracks and displays analytics for sent emails.

How it Works:

1. The backend(/backend) handles:
 -> Flask routes for managing email sending, scheduling and analytics
 -> Email content generation using OpenAI
 -> Files processing for CSV and Google Sheets

2. The frontend (/frontend) provides a dashboard to interact with the API (optional, for future enhancement).
3. Sensitive data, like API keys and SMTP credentials, is stored in a configuration file (config.py) but not included in the repository.

Setup and Usage:

1. Clone the repository
2. Set up dependencies
3. Configure sensitive information (replace placeholders in config.py)
4. Run the flask server.
5. Test the API.

What Must Be Replaced to Use the Project
SMTP Credentials:
Update SMTP_CONFIG in config.py with your email and SMTP server details.
OpenAI API Key:
	Add your OpenAI API key in config.py (OPENAI_API_KEY).
Google Sheets Credentials:
	If using Google Sheets, create a service account in Google Cloud Console and download the creds.json file.
	Update the path to creds.json in backend/data_loader.py.

gitignore:
	Ensure config.py and creds.json are excluded to prevent exposing sensitive data.

EXAMPLE PAYLOADS:
Single email:
	{
  	    "recipient": "user@example.com",
  	    "subject": "Hello!",
  	    "content": "This is a personalized message."
	}

Multiple emails:
	{
  	    "subject": "Hello!",
            "prompt_template": "Hi {name}, here’s your update!",
            "recipients": [
                    {"Email": "user1@example.com", "name": "User One"},
                    {"Email": "user2@example.com", "name": "User Two"}
            ]
        }

KNOWN ISSUES AND FUTURE ENHANCEMENTS:
Quota Limits:  Ensure OpenAI API usage stays within your allocated quota.
Error Handling: Current implementation captures errors but could provide more detailed responses.
Frontend Dashboard: Add a complete UI for easier interaction with the API.



