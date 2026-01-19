import gradio as gr
from app.config import client, MODEL, SYSTEM_PROMPT
from app.rag import retrieve

def chat(message, history):
    context = "\n\n".join(retrieve(message))

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT + "\n\nContext:\n" + context},
        {"role": "user", "content": message}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    gr.ChatInterface(chat).launch()
