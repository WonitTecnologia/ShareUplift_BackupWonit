import os
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext

class SharePointClient:
    def __init__(self, config):
        self.config = config
        self.ctx_auth = AuthenticationContext(self.config.site_url)
        if self.ctx_auth.acquire_token_for_user(self.config.username, self.config.password):
            self.ctx = ClientContext(self.config.site_url, self.ctx_auth)
            self.ctx.execute_query()
            print("Autenticado com sucesso no SharePoint!")
        else:
            print("Falha na autenticação no SharePoint!")
            exit()

    async def upload_large_file_async(self, file_path, file_name):
        try:
            file_size = os.path.getsize(file_path)
            chunk_size = 1024 * 1024 * 100  # 100 MB por parte

            with open(file_path, 'rb') as file_obj:
                target_folder = self.ctx.web.get_folder_by_server_relative_url(self.config.folder_url)
                file_info = target_folder.upload_file(file_name, file_obj.read(chunk_size))
                self.ctx.execute_query()

                uploaded_bytes = chunk_size
                while uploaded_bytes < file_size:
                    chunk = file_obj.read(chunk_size)
                    if not chunk:
                        break
                    target_folder.upload_file(file_name, chunk)
                    uploaded_bytes += len(chunk)
                    self.ctx.execute_query()
                    print(f'Uploaded {uploaded_bytes} of {file_size} bytes')

            print(f'Arquivo {file_name} enviado com sucesso para o SharePoint!')

        except Exception as e:
            print(f'Erro ao enviar o arquivo: {str(e)}')
        finally:
            # Garante a remoção do arquivo temporário, independentemente de sucesso ou erro
            os.remove(file_path)