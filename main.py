import os
import shutil

# 1. Defina o caminho da pasta que será organizada (mude para o seu caminho)
PASTA_ALVO = os.path.expanduser("~/Downloads")

# 2. Defina o mapeamento de extensões para suas respectivas pastas
MAPA_EXTENSOES = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Vídeos": [".mp4", ".mkv", ".avi", ".mov"],
    "Compactados": [".zip", ".rar", ".7z", ".tar"],
    "Instaladores": [".exe", ".msi", ".dmg"]
}

def organizar_pasta():
    # Garante que a pasta alvo existe
    if not os.path.exists(PASTA_ALVO):
        print(f"A pasta {PASTA_ALVO} não foi encontrada.")
        return

    # Varre todos os arquivos da pasta
    for arquivo in os.listdir(PASTA_ALVO):
        caminho_completo = os.path.join(PASTA_ALVO, arquivo)

        # Ignora se for uma pasta
        if os.path.isdir(caminho_completo):
            continue

        # Pega a extensão do arquivo em letras minúsculas
        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        # Descobre para qual pasta o arquivo deve ir
        pasta_destino = "Outros"
        for nome_pasta, extensoes_suportadas in MAPA_EXTENSOES.items():
            if extensao in extensoes_suportadas:
                pasta_destino = nome_pasta
                break

        # Cria a pasta de destino se ela não existir
        caminho_pasta_destino = os.path.join(PASTA_ALVO, pasta_destino)
        if not os.path.exists(caminho_pasta_destino):
            os.makedirs(caminho_pasta_destino)

        # Move o arquivo para a nova pasta
        shutil.move(caminho_completo, os.path.join(caminho_pasta_destino, arquivo))
        print(f"Movido: {arquivo} -> {pasta_destino}")

if __name__ == "__main__":
    print("Iniciando a organização...")
    organizar_pasta()
    print("Organização concluída!")
