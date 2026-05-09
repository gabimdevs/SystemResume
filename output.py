import json

# aqui salvamos o resultado num arquivo
def save_data(data):
    # "w" modo escrita, se não existir → cria arquivo, se existir → substitui
    with open("output.json", "w") as f:
        # transforma dicionário Python em JSON
        json.dump(data, f, indent=4)