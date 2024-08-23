import requests

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2-large"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        response_json = response.json()
        print("Respuesta completa de la API:", response_json)  # Imprime la respuesta completa
        return response_json
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return {}

def generar_respuesta(prompt):
    try:
        data = query({"inputs": prompt})
        print("Datos procesados:", data)  # Imprime los datos procesados antes de acceder a las claves
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict) and "generated_text" in data[0]:
            return data[0]['generated_text']
        elif isinstance(data, dict) and "generated_text" in data:
            return data['generated_text']
        else:
            return "No se pudo generar una respuesta."
    except Exception as e:
        return f"Error al generar la respuesta: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    prompt_usuario = input("Describe tu situación emocional o pregunta: ")
    respuesta = generar_respuesta(prompt_usuario)
    print("Consejo de amigo:", respuesta)
