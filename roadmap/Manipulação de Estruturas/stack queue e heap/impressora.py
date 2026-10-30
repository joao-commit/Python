from collections import deque

def imprimir_documento(documentos):
    while documentos:
        documento = documentos.popleft()
        print(f"Imprimindo: {documento}...")

documentos = deque([
    "Trabalho.pdf",
    "Curriculo.pdf",
    "Relatorio.docx",
    "Foto.png"
])

imprimir_documento(documentos)