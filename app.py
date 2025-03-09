from google import genai
import os
from dotenv import load_dotenv

# Load this environment variable from .env
load_dotenv()

# Get the Gemini API key from the environment variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# check if the API key is set
if not GEMINI_API_KEY:
    print("Error: Gemini api key environment variable is not set")
    exit()

while True:
    prompt = input("Enter your prompt: ")

    # initialize the Gemini client with the api key missiing
    client = genai.Client(api_key=GEMINI_API_KEY)

    try:
        res = client.models.generate_content(
            model='gemini-2.0-flash', contents=prompt
        )
        if prompt == 'quit':
            break
        else:
            print(res.text)
    except Exception as e:
        print(f"An error occurred: {e}")