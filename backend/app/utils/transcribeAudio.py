import whisper

def transcribe_audio(audio_path):
    """Transcreve o áudio usando Whisper e retorna o texto e os tempos."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, verbose=True)
    return result
