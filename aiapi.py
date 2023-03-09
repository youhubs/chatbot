import openai
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY


def getChatResponse(prompt):
    """Return the response to a chat message."""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)
    try:
        answer = response["choices"][0]["message"]["content"].replace("\n", "<br>")
    except IndexError:
        answer = "Oops, I didn't get that. Please try again."
    return answer
