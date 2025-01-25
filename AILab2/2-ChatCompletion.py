from openai import OpenAI

client = OpenAI(
  api_key="sk-fffffffffffffffffffff",
  base_url="http://....." # proxy base url
)

response = client.chat.completions.create(
  model="llama3.2:latest",
  messages = [
      {
          "role": "user",
          "content": prompt
      }
  ]
)
print(response)
print(response.choices[0].message.content)