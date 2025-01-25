
from openai import OpenAI

client = OpenAI(
  api_key="sk-fffffffffffffffffffff",
  base_url="http://....." # proxy base url
)


prompt = input("Hola,como te puedo ayudar? ")

response = client.chat.completions.create(
  model="llama3.2:latest",
  messages = [
      {
          "role": "user",
          "content": "Para comprobar el funcionamiento vamos a escribir un poema sobre arduino"
      }
  ]
)
print(response.choices[0].message.content)
