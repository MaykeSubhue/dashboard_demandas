import os
import shutil
from datetime import datetime

def backup_banco_dados():
    # Diretórios
    caminho_banco = 'data\demandas.db'
    pasta_backup = 'backup'

    # Criação da pasta de backup se não existir
    if not os.path.exists(pasta_backup):
        os.makedirs(pasta_backup)

    # Nome do arquivo de backup com data e hora
    data_hora_atual = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    nome_backup = f'demandas_backup_{data_hora_atual}.db'
    caminho_backup = os.path.join(pasta_backup, nome_backup)

    # Realiza o backup copiando o arquivo
    try:
        shutil.copy2(caminho_banco, caminho_backup)
        print(f'Backup realizado com sucesso: {caminho_backup}')
    except Exception as e:
        print(f'Erro ao realizar o backup: {e}')

# Testar o backup manualmente (pode ser agendado para execução automática)
if __name__ == '__main__':
    backup_banco_dados()
