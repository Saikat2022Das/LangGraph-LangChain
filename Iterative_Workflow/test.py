import os

from langchain.chat_models import init_chat_model

from dotenv import load_dotenv
load_dotenv()

# diagnostic: show which credentials are being used
print("GOOGLE_APPLICATION_CREDENTIALS:", os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
print("GOOGLE_API_KEY present:", bool(os.environ.get("GOOGLE_API_KEY")))

model = init_chat_model(
    model="google_genai:gemini-2.5-flash-lite",  # corrected typo 'flahs' -> 'flash'
    temperature=1.0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

response = model.invoke("Tell me history about Capital of India, in 3 lines?").content
print(response)