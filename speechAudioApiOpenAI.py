from pathlib import Path
from openai import OpenAI
from nicegui import ui

# Tu clave API de OpenAI
apiKey = "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"

# Inicializa el cliente de OpenAI
client = OpenAI(api_key=apiKey)

# Opciones de voces disponibles
voces = ["alloy", "athena", "eos"]

def generar_audio(voz_seleccionada, mensaje):
    try:
        # Ruta para guardar el archivo de audio
        speech_file_path = Path(__file__).parent / "speech.mp3"

        # Solicita la generación de audio a OpenAI
        response = client.audio.speech.create(
            model="tts-1",
            voice=voz_seleccionada,
            input=mensaje,
        )

        # Guarda el archivo de audio
        response.write_to_file(speech_file_path)
        ui.notify(f"Audio generado con éxito usando la voz '{voz_seleccionada}'", color="green")
    except Exception as e:
        ui.notify(f"Error al generar el audio: {str(e)}", color="red")

# Interfaz de usuario
with ui.card():
    ui.label("Generador de voces con OpenAI").classes("text-xl font-bold mb-4")

    # Selección de voz
    voz_seleccionada = ui.select(voces, label="Selecciona una voz", value="alloy").classes("mb-4")

    # Campo para ingresar el texto
    mensaje = ui.input(label="Escribe el mensaje").classes("mb-4")

    # Botón para generar el audio
    ui.button("Generar Audio", on_click=lambda: generar_audio(voz_seleccionada.value, mensaje.value)).classes("mt-4")

# Ejecuta la aplicación de NiceGUI
ui.run()
