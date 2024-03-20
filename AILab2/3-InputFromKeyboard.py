
from openai import OpenAI

client = OpenAI(
  api_key="sk-XtTqlt2gOnGIXgwH93Da2A",
  base_url="https://ailab.makespacemadrid.org" # proxy base url
)


prompt = input("Hola,como te puedo ayudar? ")

response = client.chat.completions.create(
  model="vicuna:7b-v1.5",
  messages = [
      {
          "role": "user",
          "content": "Para comprobar el funcionamiento vamos a escribir un poema sobre arduino"
      }
  ]
)
print(response.choices[0].message.content)
