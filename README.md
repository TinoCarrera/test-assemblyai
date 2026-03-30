# 🎙️ Transcriptor Universal-3 Pro (AssemblyAI)

Herramienta de línea de comandos en Python para transcribir archivos de audio locales utilizando el modelo de última generación **Universal-3 Pro** de AssemblyAI. Diseñado específicamente para pruebas de precisión y comparación frente a Deepgram Nova-3.

---

## 🚀 Características
* **Modelo de Vanguardia:** Utiliza `universal-3-pro` optimizado para español y términos técnicos.
* **Seguridad:** Gestión de credenciales mediante archivos `.env` (no expone claves en el código).
* **Automatización:** Genera archivos de texto formateados automáticamente en la carpeta de salida.
* **Flexibilidad:** Acepta argumentos directos desde la terminal para procesar diferentes archivos.

---

## 🛠️ Instalación y Configuración

Sigue estos pasos para configurar tu entorno en Windows:

1.  **Clonar/Descargar** este proyecto en una carpeta local.
2.  **Crear el entorno virtual**:
  ```cmd
  python -m venv .venv
  ```
3.  **Activar el entorno**:
  ```cmd
  .venv\Scripts\activate
  ```
4.  **Instalar dependencias**:
  ```cmd
  pip install -r requirements.txt
  ```
5.  **Configurar la API Key**:
  Crea un archivo llamado `.env` en la raíz del proyecto y añade tu clave:
  ```env
  ASSEMBLYAI_API_KEY=tu_api_key_aqui
  ```

---

## 📂 Estructura del Proyecto

```text
├── inputs/               # Coloca aquí tus audios (.mp3, .wav, etc.)
├── outputs/              # Aquí aparecerán tus transcripciones (.txt)
├── .env                  # Configuración de API Key (ignorado por Git)
├── .gitignore            # Configuración para no subir archivos basura
├── requirements.txt      # Librerías necesarias
└── test_assembly.py      # Script principal de ejecución
```

## 📖 Modo de Uso

Para procesar un archivo de audio, asegúrate de que el archivo esté guardado dentro de la carpeta `inputs/` y que tu entorno virtual esté activo.

### 1. Ejecución básica
Desde la terminal, ejecuta el script pasando el nombre del archivo como argumento:

```cmd
python test_assembly.py test_1.mp3
```
