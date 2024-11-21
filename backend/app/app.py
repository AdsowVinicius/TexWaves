from flask import Flask, request, jsonify
from utils import *
from utils.generateStrFileVideo import generate_str_file_and_video
app = Flask(__name__)

@app.route('/open-api', methods=['GET'])
def open_api():
    return jsonify({"message": "Access granted to everyone!"})
@app.route('/process_video', methods=['POST'])

def process_video():
    try:
        # Recebendo os dados do JSON enviado pelo frontend
        data = request.get_json()
        
        # Obtendo os parâmetros
        video_path = data.get('video_path')
        backend_directory = data.get('backend_directory')
        output_video_name = data.get('output_video_name')

        # Chamando a função para gerar o arquivo .str e vídeo
        str_file_path, output_video_path, video_hash = generate_str_file_and_video(video_path, backend_directory, output_video_name)

        # Preparando a resposta com o caminho dos arquivos gerados e o hash do vídeo
        response = {
            'status': 'success',
            'video_hash': video_hash,
            'str_file': str_file_path,
            'output_video': output_video_path
        }
        return jsonify(response), 200  # Retornando resposta com status 200 (OK)

    except Exception as e:
        # Caso ocorra algum erro, retornamos uma resposta de erro
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

