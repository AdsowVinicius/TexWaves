import os
from audioExtract import extract_audio_from_video
from CreateVideoWinthSubtitles import create_video_with_subtitles
from detectPauses import detect_pauses
from transcribeAudio import transcribe_audio
import os
import hashlib
from datetime import datetime

def generate_str_file_and_video(video_path, backend_directory, name_output):
    # Configuração de diretórios
    subtitles_dir = os.path.join(backend_directory, 'videosSubtitles')
    os.makedirs(subtitles_dir, exist_ok=True)

    # Gerar hash único baseado no conteúdo do vídeo
    with open(video_path, 'rb') as video_file:
        video_hash = hashlib.sha256(video_file.read()).hexdigest()[:10]

    # Caminhos dos arquivos de saída
    output_video_path = os.path.join(subtitles_dir, f"{video_hash}_{name_output}")
    str_file_path = os.path.join(subtitles_dir, f"{video_hash}.str")

    # Passo 1: Extrair áudio do vídeo
    audio_path = os.path.join(subtitles_dir, "temp_audio.wav")
    extract_audio_from_video(video_path, audio_path)

    # Passo 2: Detectar pausas no áudio
    pauses = detect_pauses(audio_path)

    # Passo 3: Transcrever o áudio
    transcribed_result = transcribe_audio(audio_path)
    segments = transcribed_result['segments']

    # Passo 4: Criar legendas com base nos segmentos transcritos
    subtitles = []
    for segment in segments:
        start_time = segment['start']
        end_time = segment['end']
        text = segment['text']
        subtitles.append((start_time, end_time, text))

    # Passo 5: Criar arquivo .str
    with open(str_file_path, 'w') as f:
        for start, end, text in subtitles:
            f.write(f"{start:.3f} --> {end:.3f}\n")  # Tempo em segundos
            f.write(f"{text}\n\n")

    # Passo 6: Criar novo vídeo com legendas
    font_path = "C:\\Windows\\Fonts\\Arial.ttf"  # Caminho para a fonte Arial no Windows
    create_video_with_subtitles(video_path, subtitles, output_video_path, font_path)


    # Limpeza: Remover arquivo de áudio temporário
    os.remove(audio_path)

    print(f"Arquivo .str salvo em: {str_file_path}")
    print(f"Novo vídeo salvo em: {output_video_path}")
    return str_file_path, output_video_path, video_hash
backend_path = r"C:\Users\adsow\OneDrive\Desktop\TexWaves\backend"
video_path = r"C:\Users\adsow\OneDrive\Desktop\TexWaves\backend\uploads\VideoTesteMoviePy.mp4"
output_video_name = "teste1.mp4"

generate_str_file_and_video(video_path, backend_path, output_video_name)