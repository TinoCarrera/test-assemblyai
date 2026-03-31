import os
import argparse
import assemblyai as aai
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("ASSEMBLYAI_API_KEY")

if not api_key:
  raise ValueError("Error: No se encontró ASSEMBLYAI_API_KEY en el archivo .env")

aai.settings.api_key = api_key

parser = argparse.ArgumentParser(description="Transcriptor Pro con AssemblyAI")

parser.add_argument("archivo", help="Nombre del archivo en la carpeta inputs/")

parser.add_argument("-p", "--prompt",
                    help="Instrucciones para identificar hablantes",
                    default="Identifica a los hablantes en la conversación.")

parser.add_argument("-d", "--dict",
                    help="Palabras clave separadas por coma",
                    default="")

args = parser.parse_args()

input_value = args.archivo

is_url = input_value.startswith(("http://", "https://"))

if is_url:
  audio_source = input_value
  file_without_ext = "remote_audio_" + input_value.split("/")[-1][:20]
else:
  audio_source = os.path.join("inputs", input_value)
  file_without_ext = os.path.splitext(input_value)[0]

  if not os.path.exists(audio_source):
    print(f"Error: El archivo local '{audio_source}' no existe.")
    exit(1)

output_dir = "outputs"
output_file = os.path.join(output_dir, f"full_data_{file_without_ext}.json")

if not os.path.exists(output_dir):
  os.makedirs(output_dir)

word_boost = args.dict.split(",") if args.dict else []

config = aai.TranscriptionConfig(
  speech_models=["universal-3-pro", "universal-2"],
  language_detection=True,
  speaker_labels=True,
  prompt=args.prompt,
  word_boost=word_boost,
  boost_param="high"
)

transcript = aai.Transcriber(config=config).transcribe(audio_source)

print("Transcripción en progreso...")

if transcript.status == "error":
  raise RuntimeError(f"Error en la transcripción: {transcript.error}")

try:
  full_data = transcript.json_response

  with open(output_file, "w", encoding="utf-8") as f:
    json.dump(full_data, f, indent=4, ensure_ascii=False)

  print(f"Datos completos guardados en: {output_file}")

except Exception as e:
  print(f"Error al guardar los datos completos: {e}")
