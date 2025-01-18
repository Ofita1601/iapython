from openai import OpenAI
apiKey = "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"
client = OpenAI(api_key= apiKey)

audio_file= open("audio.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

print(transcription.text)