from openai import OpenAI
import json

client = OpenAI(
  api_key="sk-XtTqlt2gOnGIXgwH93Da2A",
  base_url="https://ailab.makespacemadrid.org" # proxy base url
)

model_list = client.models.list()
print(model_list)
