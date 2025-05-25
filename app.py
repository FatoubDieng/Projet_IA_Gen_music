import gradio as gr
from core import generate_song


# Styles musicaux disponibles
ambiences = ["Lofi", "Mbalakh", "Rap", "Triste", "Épique", "Afro", "Piano"]

with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align:center'>Tape tes mots.<br>Écoute ta musique.</h1>")

    text_input = gr.Textbox(placeholder="Raconte-moi une histoire...", lines=4)
    ambiance = gr.Radio(ambiences, value="Lofi")

    generate_btn = gr.Button("🎵 Générer ma chanson")

    output_text = gr.Textbox(label="Texte analysé", interactive=False)
    audio_output = gr.Audio(label="🎧 Ta chanson", autoplay=True)

    download_btn = gr.File(label="Télécharger ta chanson", file_types=[".mp3"])

    generate_btn.click(fn=generate_song,
                       inputs=[text_input, ambiance],
                       outputs=[output_text, audio_output, download_btn])

demo.launch()