from nicegui import ui
from openai import OpenAI

class ChatApp:
    def __init__(self):
        # Configura tu API key de OpenAI aquí
        apiKey = "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"
        self.client = OpenAI(api_key=apiKey)
        self.messages = []
        self.setup_ui()

    def setup_ui(self):
        # Contenedor principal
        with ui.column().classes('w-full max-w-3xl mx-auto p-4 space-y-4'):

            # Título con posición fija
            ui.label('Chat con OpenAI').classes(
                'text-2xl font-bold text-center bg-white py-2 shadow-md sticky top-0 z-10'
            )

            # Contenedor de mensajes
            with ui.card().classes('w-full p-4 bg-gray-50 shadow-md h-96 overflow-auto'):
                self.chat_container = ui.column().classes('w-full space-y-4')

            # Área de entrada y botón
            with ui.row().classes('w-full gap-2'):
                self.input = ui.input(placeholder='Escribe tu mensaje...').classes(
                    'w-full border border-gray-300 rounded-lg p-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400'
                )
                ui.button('Enviar', on_click=self.send_message).classes(
                    'bg-blue-500 hover:bg-blue-600 text-white font-medium px-4 py-2 rounded-lg shadow-md'
                )

            # Enviar mensaje con la tecla Enter
            self.input.on('keydown.enter', self.send_message)

    async def send_message(self):
        user_message = self.input.value
        if not user_message.strip():
            return

        # Limpiar input
        self.input.value = ''

        # Mostrar mensaje del usuario
        with self.chat_container:
            ui.chat_message(
                text=user_message, name='Tú', sent=True
            ).classes('bg-blue-100 p-2 rounded-lg shadow-sm')

        # Preparar el contexto del chat
        messages = [
            {"role": "system", "content": "Eres un asistente útil y devuelve las respuestas en Español"},
            {"role": "user", "content": user_message}
        ]
        
        try:
            # Obtener respuesta de OpenAI
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            assistant_message = response.choices[0].message.content

            # Mostrar respuesta del asistente
            with self.chat_container:
                ui.chat_message(
                    text=assistant_message, name='Asistente', sent=False
                ).classes('bg-gray-100 p-2 rounded-lg shadow-sm')

        except Exception as e:
            with self.chat_container:
                ui.label(f'Error: {str(e)}').classes('text-red-500')

# Iniciar la aplicación
chat = ChatApp()
ui.run(title='Chat con IA', port=8080, reload=True)
