from google import genai
from apikey import api_key

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"write an email for my boss to let him know that i am quiting my job",
)
print(response.text)
