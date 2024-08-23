import requests

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2-large"
headers = {"Authorization": "Bearer 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"}

def generar_articulo(prompt):
    try:
        # Enviar solicitud a la API
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        response_json = response.json()
        print("Respuesta completa de la API:", response_json)  # Imprime la respuesta completa
        
        # Verificar y extraer el texto generado
        if isinstance(response_json, dict) and "generated_text" in response_json:
            return response_json['generated_text']
        elif isinstance(response_json, list) and len(response_json) > 0 and "generated_text" in response_json[0]:
            return response_json[0]['generated_text']
        else:
            return "No se pudo generar el artículo."
    except requests.exceptions.RequestException as e:
        return f"Error al generar el artículo: {e}"

# Ejemplo de uso
if __name__ == "__main__":
    prompt = "Escribe un artículo de 1000 palabras sobre cómo gestionar la ansiedad, incluyendo técnicas de respiración, ejercicios de relajación y consejos prácticos."
    articulo = generar_articulo(prompt)
    print("Artículo generado:", articulo)
