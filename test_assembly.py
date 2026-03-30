import os
import assemblyai as aai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ASSEMBLYAI_API_KEY")

if not api_key:
  raise ValueError("¡Error! No se encontró ASSEMBLYAI_API_KEY en el archivo .env")

aai.settings.api_key = api_key

audio_file = os.path.join("assets", "test_2.mp3")

if not os.path.exists(audio_file):
  raise FileNotFoundError(f"No se encontró el archivo en: {audio_file}")

# Uses universal-3-pro for en, es, de, fr, it, pt. Else uses universal-2 for support across all other languages
config = aai.TranscriptionConfig(speech_models=["universal-3-pro", "universal-2"], language_detection=True)

transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

print("-" * 30)
print("TRANSCRIPCIÓN LOCAL COMPLETADA:")
print("-" * 30)
print(transcript.text)
print("-" * 30)
print(f"Confianza: {transcript.confidence:.2%}")
