import subprocess

# Caminho para o executável do FFmpeg dentro do projeto
ffmpeg_path = r"C:\Users\adsow\OneDrive\Desktop\TexWaves\backend\ffmpeg\bin\ffmpeg.exe"

# Exemplo de uso do FFmpeg com o caminho completo
subprocess.run([ffmpeg_path, "-version"])
