import re

def normalize_text(texto):
    texto = texto.lower()
    texto = re.sub(r"[!?;:]", "", texto)
    texto = re.sub(r"\s+",  " ", texto)
    return texto.strip()