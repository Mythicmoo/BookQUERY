import PyPDF2
import os
from tqdm import tqdm

# Relaciona a O BD_PDF com as Variáveis do Programa
Arquivos_PDF = os.listdir('Acervo')

# Pergunta o Termo a ser pesquisado
passe = input(str('Qual referência você está procurando ? \n '))

print(2*'/n')

# Cria a lista de referências que serão usadas na resposta final
referencia = {}
for a in Arquivos_PDF:
    referencia[f'{a}'] = []

# Testa para cada arquivo se existe o termo procurado em suas páginas
for i in Arquivos_PDF:
    nome_arquivo = i
    arquivo = f"Acervo\{nome_arquivo}"
    lerpdf = PyPDF2.PdfFileReader(arquivo, strict=False)
    numero_paginas = lerpdf.getNumPages()

    # Testa se existe o termo referenciado na página , se existir ele é adicionado em refeências
    for p in tqdm(range(0, numero_paginas)):
        pagina = lerpdf.getPage(p)
        conteudo = pagina.extractText()
        if passe.lower() in conteudo.lower():
            referencia[f'{i}'].append(p+1)

print(2*'/n')

# Informa o usuário em quais páginas as referências foram encontradas
for k, c in referencia.items():
    print(f'Na Obra \033[1;31;40m{k}\033[m foram encontradas referências nas seguintes páginas \n {c}')