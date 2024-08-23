import requests

API_KEY = '3f657d8b-07d4-4d89-9da1-e57c2134c847'  
IMAGE_API_URL = 'https://api.deepai.org/api/text2img'  

def generate_image(prompt):
    headers = {
        'api-key': API_KEY
    }
    data = {
        'text': prompt
    }
    try:
        # Realizar la solicitud POST a la API
        response = requests.post(IMAGE_API_URL, data=data, headers=headers)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        response_json = response.json()
        print("Respuesta completa de la API de imagen:", response_json)  # Imprimir la respuesta completa
        image_url = response_json.get('output_url', '')
        return image_url
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return ''

# Ejemplo de uso
prompt = "Una ilustración de una red de apoyo emocional."
image_url = generate_image(prompt)
print(f"URL de la imagen generada: {image_url}")
