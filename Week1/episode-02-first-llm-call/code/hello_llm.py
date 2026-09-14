"""Episode 02 — first LLM call.

Authenticates to OpenAI, sends one message, prints the reply.
"""

# --- 1. Imports -------------------------------------------------------------
# TODO: you need three things here:
#   - the standard-library module for reading environment variables
#   - load_dotenv, from the dotenv package
#   - the OpenAI class, from the openai package

import os
from dotenv import load_dotenv
from openai import OpenAI


# --- 2. Load the API key ----------------------------------------------------
# TODO:
#   a) call load_dotenv() to read the .env file into the process environment
#   b) read OPENAI_API_KEY out of the environment into a variable
#   c) if it is missing, raise a ValueError with a clear message
#      (fail loudly and early — do not let a None key reach the API call)


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Please set it in your .env file.")


# --- 3. Create the client ---------------------------------------------------
# TODO: construct an OpenAI client, passing the api_key you just read.

client  = OpenAI(api_key=api_key)   


# --- 4. Define the model and the prompt -------------------------------------
# TODO: two variables — the model identifier string, and the question to ask.
#       Pulling these out as named variables (rather than inlining them below)
#       keeps the call readable and makes them easy to change.

model = "gpt-4o-mini"
question = "How is Virat Kohli?"


# --- 5. Build the messages list ---------------------------------------------
# TODO: the API expects a LIST of messages, even when sending only one.
#       Each message is a dict with exactly two keys: "role" and "content".
#       Role for a question you are asking is "user".

message = {"role": "user", "content": question} 
messages = [message]

# --- 6. Make the call -------------------------------------------------------
# TODO: client.chat.completions.create(...), passing model and messages
#       as keyword arguments. Assign the result to `response`.

response = client.chat.completions.create(
    model=model,
    messages=messages
)



# --- 7. Print the reply -------------------------------------------------------
# TODO:
#   a) print the reply text. It lives at:  response.choices[0].message.content
#   b) print the token usage:              response.usage
#      (we care about cost — see why below)


print(response.choices[0].message.content)
print(response.usage)