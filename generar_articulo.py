from api_chat import generate_text_response, generate_image

def create_article_with_image(text_prompt, image_prompt):
    text_response = generate_text_response(text_prompt)
    image_url = generate_image(image_prompt)
    
    article = f"Artículo generado:\n{text_response}\n\nImagen asociada:\n{image_url}"
    
    return article

# Ejemplo de uso
text_prompt = "Escribe un artículo sobre la importancia del apoyo emocional."
image_prompt = "Imagen conceptual sobre apoyo emocional"

article = create_article_with_image(text_prompt, image_prompt)
print(article)
