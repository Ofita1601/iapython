from nicegui import ui
from openai import OpenAI

apiKey = "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"

client = OpenAI(api_key= apiKey)

def load_audio(file:str):
    audio_file= open(file, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )      

    with ui.card().tight():
        a = ui.audio(file)
        a.on('ended', lambda _: ui.notify('Audio playback completed'))

        with ui.card_section():
             ui.label(transcription.text)

ui.upload(on_upload=lambda e: load_audio(e.name)).classes('max-w-full')

ui.run()