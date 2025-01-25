import requests
import openai

client = openai.OpenAI(
  api_key="sk-",
  base_url="https://iapi" # proxy base url
)

# 2. Generar una imagen con DALL·E
response = client.images.generate(
    prompt="Un paisaje surrealista con montañas de colores brillantes y un cielo púrpura",
    model="dall-e-2"
)

print(response)

