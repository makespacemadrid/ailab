from openai import OpenAI

client = OpenAI(
  api_key="sk-XtTqlt2gOnGIXgwH93Da2A",
  base_url="https://ailab.makespacemadrid.org" # proxy base url
)

response = client.chat.completions.create(
  model="vicuna:7b-v1.5",
  messages = [
      {
          "role": "user",
          "content": prompt
      }
  ]
)
print(response)
print(response.choices[0].message.content)