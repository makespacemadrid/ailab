
from openai import OpenAI
import requests


client = OpenAI(
  api_key="sk-fffffffffffffffffffff",
  base_url="http://....." # proxy base url
)


master_prompt = "Eres una IA que ayuda a los usuarios de MakeSpace durante el taller de AiLab"
assistant_prompt = "Hola Maker! Como te puedo ayudar?"


def getExtraInfo():
    # Realizar una solicitud GET a la URL
    response = requests.get("https://spaceapi.makespacemadrid.org")

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el contenido JSON de la respuesta
        data = response.json()

        # Extraer campos relevantes
        space_name = data.get("space", "N/A")
        space_url = data.get("url", "N/A")
        location = data.get("location", {})
        address = location.get("address", "N/A")
        lat = location.get("lat", "N/A")
        lon = location.get("lon", "N/A")
        contact = data.get("contact", {})
        phone = contact.get("phone", "N/A")
        email = contact.get("email", "N/A")
        state = data.get("state", {})
        is_open = state.get("open", False)
        open_status = "Espacio Abierto" if is_open else "Espacio Cerrado"
        sensors = data.get("sensors", {})
        sensor_info = []

        for sensor_type, sensor_list in sensors.items():
            for sensor in sensor_list:
                sensor_name = sensor.get("name", "N/A")
                sensor_value = sensor.get("value", "N/A")
                sensor_unit = sensor.get("unit", "")
                sensor_location = sensor.get("location", "N/A")
                sensor_info.append(f"{sensor_name} ({sensor_type}, {sensor_location}): {sensor_value} {sensor_unit}")
        # Crear una cadena con los campos relevantes y sus valores, incluyendo el estado de apertura/cierre
        info_str = f"Reporte actualizado del sistema domotico con el estado del espacio MakeSpace Madrid: Space Name: {space_name}\nSpace URL: {space_url}\nAddress: {address}\nLatitude: {lat}\nLongitude: {lon}\nPhone: {phone}\nEmail: {email}\nStatus: {open_status}\nSensors:\n{', '.join(sensor_info)}"
        return info_str



additional_info = getExtraInfo()
combined_master_prompt = master_prompt + '/n' + additional_info
print("\n\n")


prompt = input(assistant_prompt)

response = client.chat.completions.create(
  model="llama3.2:latest",
  messages = [
      {
          "role": "system",
          "content": combined_master_prompt
      },
      {
          "role": "assistant",
          "content": assistant_prompt
      },
      {
          "role": "user",
          "content": prompt
      }
  ]
)
print(response.choices[0].message.content)
