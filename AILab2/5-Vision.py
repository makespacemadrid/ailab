import openai
from openai import OpenAI

import base64


client = OpenAI(base_url='https://iapi',api_key='sk-')
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Allen_keys.jpg/800px-Allen_keys.jpg"


response = client.chat.completions.create(model="llama3.2-vision:latest",
messages=[
        {"role": "user", "content": "Genera una descripción corta y concisa del objeto de la imagen, 3-5 palabras. Responde solo con el nombre del objeto en español."},
        {"role": "user", "content": f"<image>{image_url}</image>"}  # El formato correcto para pasar una imagen URL
    ]
)

# Imprime la respuesta
message_content = response.choices[0].message.content
print(message_content)