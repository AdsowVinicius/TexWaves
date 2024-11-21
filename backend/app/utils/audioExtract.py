import moviepy.editor as mp

def extract_audio_from_video(video_path, audio_path):
    """Extrai o áudio do vídeo e salva em um arquivo."""
    video_clip = mp.VideoFileClip(video_path)
    video_clip.audio.write_audiofile(audio_path)
    return audio_path