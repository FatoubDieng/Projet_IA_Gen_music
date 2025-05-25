from gtts import gTTS
from pydub import AudioSegment
import gradio as gr

def generate_song(text, ambiance):
    language = 'fr'
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("voice.mp3")
    voix = AudioSegment.from_file("voice.mp3")


    if ambiance == "Lofi":
        musique = AudioSegment.from_file("lofi.mp3")
    elif ambiance == "Mbalakh":
        musique = AudioSegment.from_file("mbalakh.mp3")
    elif ambiance == "Rap":
        musique = AudioSegment.from_file("rap.mp3")
    elif ambiance == "Triste":
        musique = AudioSegment.from_file("triste.mp3")
    elif ambiance == "Épique":
        musique = AudioSegment.from_file("epique.mp3")
    elif ambiance == "Afro":
        musique = AudioSegment.from_file("afro.mp3")
    elif ambiance == "Piano":
        musique = AudioSegment.from_file("piano.mp3")
    else:
        return f"Ambiance inconnue : {ambiance}", None, None

    voix = voix + 4
    musique = musique - 3

    if musique.duration_seconds > voix.duration_seconds:
        musique = musique[:len(voix)]
    else:
        voix = voix[:len(musique)]

    mix = musique.overlay(voix)
    output_path = "final_mix.mp3"
    mix.export(output_path, format="mp3")

    return f"Tu as choisi l'ambiance {ambiance} avec ton texte :", output_path, output_path