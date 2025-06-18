import os
import openai

# Load the OpenAI API key for access
openai.api_key = os.getenv('OPENAI_API_KEY')

def ask_gpt(prompt: str, context: list = None, temperature=0.7, max_tokens=500):

    # Initial prompt to instruct model to act as an HR assistant chatbot
    messages = [{"role": "system", "content": "You are an HR assistant chatbot."}]
    if context:
        messages.extend(context)
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",                                      # Specifying the model to use
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()
