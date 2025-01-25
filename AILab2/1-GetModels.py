from openai import OpenAI
import json

client = OpenAI(
  api_key="sk-",
  base_url="http://iapi" # proxy base url
)

model_list = client.models.list()
print(model_list)
