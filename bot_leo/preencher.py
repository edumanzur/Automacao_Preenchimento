from docx import Document

def preencher_modelo(caminho_modelo, caminho_saida, dados):
    doc = Document(caminho_modelo)

    for paragrafo in doc.paragraphs:
        for chave, valor in dados.items():
            paragrafo.text = paragrafo.text.replace(f'{{{{{chave}}}}}', valor)

    for tabela in doc.tables:
        for linha in tabela.rows:
            for celula in linha.cells:
                for paragrafo in celula.paragraphs:
                    for chave, valor in dados.items():
                        paragrafo.text = paragrafo.text.replace(f'{{{{{chave}}}}}', valor)

    for section in doc.sections:
        for part in [section.header, section.footer]:
            for paragrafo in part.paragraphs:
                for chave, valor in dados.items():
                    paragrafo.text = paragrafo.text.replace(f'{{{{{chave}}}}}', valor)

    doc.save(caminho_saida)
