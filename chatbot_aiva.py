import gradio as gr
import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "system", "content": "Eres AIVA, el asistente de AIVI Solutions. Responde sobre cursos, Perceptia, certificados y servicios empresariales de manera profesional, clara y amable."}
]

def responder(user_input):
    messages.append({"role": "user", "content": user_input})
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"Error: {e}"

iface = gr.Interface(
    fn=responder,
    inputs="text",
    outputs="text",
    title="AIVA – Asistente AIVI",
    description="Haz preguntas sobre los cursos, certificados, acceso, módulos, y más."
)
