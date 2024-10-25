import os
from flask import Blueprint, request, jsonify
import asyncio
from clients.sharepoint_client import SharePointClient
from config.sharepoint_config import SharePointConfig

upload_bp = Blueprint('upload', __name__)

config = SharePointConfig(
    site_url="https://teste.sharepoint.com/",  #aqui coloca a URL do dominio do share
    username="email@teste.com.br", #email de login
    password="Senha_TOP", #senha de login
    folder_url="/Pasta/Teste" #pasta para envio
)
sharepoint_client = SharePointClient(config)

@upload_bp.route('/upload', methods=['POST'])
async def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nome do arquivo inválido'}), 400

    try:
        # Salva o arquivo temporariamente
        local_dir = os.path.dirname(os.path.realpath(__file__))
        temp_file_path = os.path.join(local_dir, '../tmp', file.filename)
        os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
        file.save(temp_file_path)

        # Envia para o SharePoint de forma assíncrona
        asyncio.create_task(sharepoint_client.upload_large_file_async(temp_file_path, file.filename))

        return jsonify({'message': f'Upload do arquivo {file.filename} iniciado em segundo plano!'}), 202
    except Exception as e:
        return jsonify({'error': f'Erro ao iniciar o upload do arquivo: {str(e)}'}), 500
