import os
import sys
import assemblyai as aai
from dotenv import load_dotenv

if len(sys.argv) < 2:
  print("Error: Debes proporcionar el nombre del archivo.")
  print("Uso correcto: python test_assembly.py nombre_del_archivo.mp3")
  sys.exit(1)

load_dotenv()

api_key = os.getenv("ASSEMBLYAI_API_KEY")

if not api_key:
  raise ValueError("Error: No se encontró ASSEMBLYAI_API_KEY en el archivo .env")

aai.settings.api_key = api_key

file_name = sys.argv[1]
audio_file = os.path.join("inputs", file_name)

if not os.path.exists(audio_file):
  raise FileNotFoundError(f"No se encontró el archivo en: {audio_file}")

file_without_ext = os.path.splitext(file_name)[0]
output_dir = "outputs"
output_file = os.path.join(output_dir, f"transcripcion_{file_without_ext}.txt")

# Uses universal-3-pro for en, es, de, fr, it, pt. Else uses universal-2 for support across all other languages
config = aai.TranscriptionConfig(speech_models=["universal-3-pro", "universal-2"], language_detection=True)

transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

if not os.path.exists(output_dir):
  os.makedirs(output_dir)
  print(f"Carpeta '{output_dir}' creada.")

try:
  with open(output_file, "w", encoding="utf-8") as f:
    f.write(transcript.text)

  print("-" * 30)
  print(f"Transcripción guardada en: {output_file}")
  print("-" * 30)

except Exception as e:
  print(f"Error al escribir el archivo: {e}")
