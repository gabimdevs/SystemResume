# importando a biblioteca que permite abrir e ler arquivos PDF usando Python
import PyPDF2
# serve para encontrar padrões dentro de textos
import re

# criando uma função chamada extract_text
# ela recebe o caminho do PDF como parâmetro
def extract_text(pdf_path):
    # abre o arquivo PDF
    # "rb" = read binary (modo leitura binária)
    # PDF não é texto simples → precisa abrir em modo binário
    # o with garante que o arquivo será fechado automaticamente depois
    with open(pdf_path, "rb") as file:
        # criou um leitor de PDF
        # agora o Python consegue “entender” o documento
        reader = PyPDF2.PdfReader(file)
        # variável vazia que vai guardar o texto extraído
        text = ""
        # um PDF pode ter várias páginas
        # esse loop percorre cada página do documento
        for page in reader.pages:
            # para cada página extraímos o texto
            # adicionamos na variável text
            text += page.extract_text()
    # devolve o texto completo do PDF
    return text

def extract_email(text):
    # procura o primeiro resultado que combine com o padrão
    match = re.search(r'\S+@\S+', text) # esse é o padrão do email (\S+@\S+)
    # se encontrou email → retorna o texto encontrado, se não encontrou → retorna None
    return match.group() if match else None

def extract_name(text):
    # procura o primeiro resultado que combine com o padrão
    match = re.search(r'\S+', text) # esse é o padrão do nome (\S+)
    # se encontrou nome → retorna o texto encontrado, se não encontrou → retorna None
    return match.group() if match else None

def extract_phone(text):
    # procura números BR
    match = re.search(r'\(?\d{2}\)?\s?\d{4,5}-?\d{4}', text)
    # se encontrou o número → retorna o texto encontrado, se não encontrou → retorna None
    return match.group() if match else None

def extract_skills(text):
    # criando uma lista com tecnologias que queremos procurar
    skills = ["Python", "Java", "React", "SQL", "Spring", "CSS", "Javascript", "HTML"]
    # para cada tecnologia converte texto para minúsculo
    # verifica se aparece no currículo, se aparecer → adiciona na lista found
    found = [skill for skill in skills if skill.lower() in text.lower()]
    return found