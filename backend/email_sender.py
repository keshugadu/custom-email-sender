from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config_template import SMTP_CONFIG
from prompt_generator import generate_email_content

def send_custom_email(data):
    try:
        # Extract common fields
        recipient = data.get("recipient")
        subject = data.get("subject")
        content = data.get("content")  # Use this if content is directly provided
        
        # Connect to the SMTP server
        smtp_server = SMTP(SMTP_CONFIG['server'], SMTP_CONFIG['port'])
        smtp_server.starttls()
        smtp_server.login(SMTP_CONFIG['email'], SMTP_CONFIG['password'])
        
        # Check if we need to use `prompt_template` and `recipients` list
        if 'prompt_template' in data and 'recipients' in data:
            prompt_template = data['prompt_template']
            for row in data['recipients']:
                email_content = generate_email_content(prompt_template, row)
                msg = MIMEMultipart()
                msg['From'] = SMTP_CONFIG['email']
                msg['To'] = row['Email']
                msg['Subject'] = subject
                msg.attach(MIMEText(email_content, 'html'))
                
                smtp_server.sendmail(SMTP_CONFIG['email'], row['Email'], msg.as_string())
        
        # If no prompt_template is provided, use the content field
        elif recipient and subject and content:
            msg = MIMEMultipart()
            msg['From'] = SMTP_CONFIG['email']
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(content, 'html'))
            
            smtp_server.sendmail(SMTP_CONFIG['email'], recipient, msg.as_string())
        else:
            return {"error": "Missing required fields"}, 400
        
        # Quit the SMTP session
        smtp_server.quit()
        return {"status": "Emails sent successfully"}
    
    except Exception as e:
        # Handle any exceptions that occur and return an error message
        return {"error": str(e)}, 500