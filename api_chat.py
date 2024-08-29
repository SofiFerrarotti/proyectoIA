import requests

# Configura tus claves API y URLs
CHAT_API_URL = 'https://api-inference.huggingface.co/models/openai-community/gpt2-large'
IMAGE_API_URL = 'https://creator.nightcafe.studio/studio?open=creation&panelContext=%28jobId%3Ap23IlEZ0u8Xz86zjMLyf%29'
CHAT_API_KEY = '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'
IMAGE_API_KEY = '3f657d8b-07d4-4d89-9da1-e57c2134c847'

def generate_text_response(prompt):
    headers = {'Authorization': f'Bearer {CHAT_API_KEY}', 'Content-Type': 'application/json'}
    data = {'inputs': prompt}  
    try:
        response = requests.post(CHAT_API_URL, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print("Respuesta completa de la API de texto:", response_json)  
        return response_json[0]['generated_text'] 
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return ''

def generate_image(prompt):
    headers = {'Authorization': f'Bearer {IMAGE_API_KEY}', 'Content-Type': 'application/json'}
    data = {'prompt': prompt}
    try:
        response = requests.post(IMAGE_API_URL, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        print("Respuesta completa de la API de imagen:", response_json)  
        image_url = response_json.get('image_url', '')
        return image_url
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return ''
