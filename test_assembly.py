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

args = parser.parse_args()

audio_file = os.path.join("inputs", args.archivo)
file_without_ext = os.path.splitext(args.archivo)[0]

output_dir = "outputs"
output_file = os.path.join(output_dir, f"full_data_{file_without_ext}.json")

if not os.path.exists(audio_file):
  print(f"Error: No existe '{audio_file}'")
  exit(1)

if not os.path.exists(output_dir):
  os.makedirs(output_dir)

config = aai.TranscriptionConfig(
  speech_models=["universal-3-pro", "universal-2"],
  language_detection=True,
  speaker_labels=True,
  prompt=args.prompt
)

transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

try:
  full_data = transcript.json_response

  with open(output_file, "w", encoding="utf-8") as f:
    json.dump(full_data, f, indent=4, ensure_ascii=False)

  print(f"Datos completos guardados en: {output_file}")

except Exception as e:
  print(f"Error al guardar los datos completos: {e}")
