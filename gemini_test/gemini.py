import os
import pyttsx3
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file, if available
load_dotenv()
API_KEY = os.getenv("GEMINI_API_TOKEN")

if not API_KEY:
    API_KEY = input("Enter your API key: ")

# Initialize the Gemini client with your API key
client = genai.Client(api_key=API_KEY)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

print("🔮 Gemini Prompt Bot - Type 'exit' to quit")

while True:
    user_prompt = input("\nEnter your prompt: ")
    if user_prompt.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_prompt,
        )
        # Remove all asterisks from the response string
        clean_response = response.text.replace("*", "")
        
        print("\nResponse:", clean_response)
        
        # Speak the cleaned response using TTS
        engine.say(clean_response)
        engine.runAndWait()
        
    except Exception as e:
        print("⚠️  Error generating content:", e)
