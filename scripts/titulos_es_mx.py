#!/usr/bin/env python3
"""Normaliza títulos de producto al estilo es-MX de la tienda.

Uso: python3 scripts/titulos_es_mx.py admin-audit/productos.json admin-audit/titulos-cambios.csv

Reglas (conservadoras, no tocan sustantivos ni nombres propios):
- Palabras de enlace en minúscula salvo al inicio: de, del, la, las, el, los, y, e, o, u, con, para, en, a, al, sin, por.
  No se toca una letra suelta después de "Letra"/"Inicial" (dijes con inicial).
- Unidades: Cm -> cm, Mm -> mm. Quilates: 10k -> 10K, 14k -> 14K, 18k -> 18K.
- Plata: "Plata 925", "Ley 925", "Esterlina 925" -> ".925" (no toca otros números).
"""
import csv, json, re, sys

CONNECTORS = {'de', 'del', 'la', 'las', 'el', 'los', 'y', 'e', 'o', 'u', 'con', 'para', 'en', 'a', 'al', 'sin', 'por'}
INITIAL_MARKERS = {'letra', 'inicial', 'letras', 'iniciales'}
TOKEN = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+|[^A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+")


def fix_title(title):
    t = title
    t = re.sub(r'\b(Plata|Ley|Esterlina)\s+925\b', r'\1 .925', t, flags=re.I)
    t = re.sub(r'(\d+(?:\.\d+)?)\s?Cm\b', r'\1 cm', t)
    t = re.sub(r'(\d+(?:\.\d+)?)\s?Mm\b', r'\1 mm', t)
    t = re.sub(r'\b(10|14|18)k\b', r'\1K', t)

    tokens = TOKEN.findall(t)
    out, seen_word, prev_word = [], False, ''
    for i, tok in enumerate(tokens):
        if tok[0].isalpha():
            low = tok.lower()
            after_separator = bool(out) and re.search(r'[|:–—]\s*$', out[-1] or '')
            if (seen_word and not after_separator and low in CONNECTORS
                    and tok != low and prev_word.lower() not in INITIAL_MARKERS
                    and not (len(tok) == 1 and i + 1 < len(tokens) and tokens[i + 1].startswith('.'))):
                tok = low
            seen_word = True
            prev_word = tok
        out.append(tok)
    return ''.join(out)


def main():
    products = json.load(open(sys.argv[1], encoding='utf-8'))
    rows = []
    for p in products:
        new = fix_title(p['title'])
        if new != p['title']:
            rows.append({'ID': p['id'].split('/')[-1], 'Handle': p['handle'], 'Title': new, 'Antes': p['title']})
    with open(sys.argv[2], 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['ID', 'Handle', 'Title', 'Antes'])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} de {len(products)} títulos cambian")


if __name__ == '__main__':
    main()
