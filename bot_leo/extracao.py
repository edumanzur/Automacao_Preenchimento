import pymupdf

def extrair_campos(pdf_path):
    with pymupdf.open(pdf_path) as data:
        text = data[0].get_text()

    linhas = text.splitlines()

    campos_referencia = {
        "PACIENTE": linhas[18],
        "NASCIMENTO": linhas[20].split(" ")[0],
        "IDADE": linhas[20].split(" ")[1][1:],
        "SEXO": linhas[21],
        "MAE": linhas[25],
        "TELEFONE": " ".join(linhas[49].split(" ")[:2]),
        "CRM": linhas[61],
        "MEDICO": linhas[62],
        "CID": linhas[68],
        "DIAGNOSTICO": linhas[67],
        "PROCEDIMENTO": linhas[81],
        "NACIONALIDADE": linhas[30],
        "CPF_MEDICO": linhas[60],
        "ENDERECO": linhas[36],
        "CEP": linhas[43],
        "RISCO": linhas[69],
        "DIAGNOSTICO_INICIAL": linhas[67],
        "CENTRAL": "Central Reguladora (None)",
        "UNIDADE": linhas[6],
        "DATA_SOLICITACAO": linhas[77],
        "SITUACAO_ATUAL": "Situação Atual (None)",
        "HOSPITAL": linhas[75],
    }
    return campos_referencia