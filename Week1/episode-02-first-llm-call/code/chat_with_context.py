from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

model = "gpt-4o-mini"

messages = [
    {
        "role" : "system", 
        "content" : "Answer in exactly one sentence. No greetings, no caveats"
    },
    {
        "role" : "user", 
        "content" : "How is Virat Kohli?"
    },
    {
        "role" : "assistant", 
        "content" : "Virat Kohli is currently regarded as one of the top cricketers in the world, known for his exceptional batting skills and leadership qualities."
    },
    {
        "role" : "user", 
        "content" : "What is his age?"
    }

]


response = client.chat.completions.create(
    model=model,
    messages=messages
)

print(response.choices[0].message.content)
print(response.usage)

