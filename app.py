import gradio as gr
from transformers import pipeline

# Load translation pipeline
translator = pipeline("translation_en_to_ar", model="Helsinki-NLP/opus-mt-en-ar")

def translate_text(text):
    result = translator(text, max_length=200)
    return result[0]['translation_text']

# Gradio Interface
iface = gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox(lines=3, placeholder="Enter text in English..."),
    outputs="text",
    title="English → Arabic Translator 🌍",
    description="Translate English text into Modern Arabic using Hugging Face Transformers + Gradio."
)

if __name__ == "__main__":
    iface.launch()
