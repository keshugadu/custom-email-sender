import openai
from config_template import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY  # Set the API key here

def generate_email_content(prompt_template, row_data):
    prompt = prompt_template.format(**row_data)
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()