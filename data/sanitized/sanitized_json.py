import json
from pathlib import Path

# Pasta com os arquivos originais
pasta_origem = Path("data/raw")

# Pasta para salvar os arquivos anonimizados
pasta_destino = Path("data/sanitized")
pasta_destino.mkdir(exist_ok=True)

# Percorrendo todos os JSONs
for arquivo in pasta_origem.glob("*.json"):
    
    # Abrindo arquivo
    with open(arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)
    
    # Removendo ip_addr de cada registro
    for registro in dados:
        registro.pop("ip_addr", None)
    
    # Salvando novo arquivo
    novo_arquivo = pasta_destino / arquivo.name
    
    with open(novo_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    
    print(f"OK: {arquivo.name}")
    
print("Anonimização concluída.")