#!/usr/bin/env python3
"""Aplica las correcciones es-MX de la auditoría a los JSON de templates y grupos de un tema.

Uso: python3 scripts/fix_es_mx.py <carpeta_del_tema> [archivo_log.tsv]

Es idempotente y trabaja por contenido (no por posición), así que puede re-aplicarse
sobre versiones nuevas del tema sin pisar cambios no relacionados.
"""
import json, re, sys, os
from collections import Counter

ROOT = sys.argv[1]
LOG_PATH = sys.argv[2] if len(sys.argv) > 2 else None
LOG, MISSING = [], []


def load(p):
    raw = open(p, encoding='utf-8').read()
    return json.loads(re.sub(r'^/\*.*?\*/\s*', '', raw, flags=re.S))


def save(p, data):
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def walk(node, path, fn):
    items = node.items() if isinstance(node, dict) else enumerate(node) if isinstance(node, list) else []
    for k, v in list(items):
        sub = f'{path}.{k}' if isinstance(node, dict) else f'{path}[{k}]'
        if isinstance(v, str):
            nv = fn(sub, v)
            if nv != v:
                node[k] = nv
        else:
            walk(v, sub, fn)


GLOBAL_SUB = [
    (">mercado libre<", ">Mercado Libre<"),
    (">Mayoreo!<", ">¡Mayoreo!<"),
    ("Pairs well with", "Combina bien con"),
    ("Productos Similares", "Productos similares"),
    ("Solícitala", "Solicítala"),
    ("<p>We are available from monday to friday to answer your questions.</p>",
     "<p>Estamos disponibles de lunes a viernes para resolver tus dudas.</p>"),
    ("<p>Your payment information is processed securely.</p>",
     "<p>Tu información de pago se procesa de forma segura.</p>"),
]
GLOBAL_EXACT = {
    "Customer service": "Atención a clientes",
    "Secure payment": "Pago seguro",
    "Mayoreo!": "¡Mayoreo!",
    "View all": "Ver todo",
    "clientes satisfechos": "Clientes satisfechos",
}

FILE_SUB = {
    'templates/index.json': [
        ("plata  que  dura", "plata que dura"),
        ("Envios a todo mexico", "Envíos a todo México"),
        ("<strong>fundicion de presición </strong>", "<strong>fundición de precisión</strong> "),
        ("México </strong>,<strong>miembro", "México</strong>, <strong>miembro "),
        ("<strong>cadenas  </strong>son", "<strong>cadenas</strong> son"),
        ("las mejores talleres de Italia y Turquía, reconocidas", "los mejores talleres de Italia y Turquía, reconocidos"),
        ("talleres de europa reconocidos", "talleres de Europa, reconocidos"),
        ("<br/><br/><br/><br/>", ""),
        ("También De venta en", "También de venta en"),
    ],
    'templates/product.productpage.json': [
        ("\n      FAQ\n", "\n      Preguntas frecuentes\n"),
    ],
    'templates/product.product-page-v2.json': [
        ("<strong>¿Expides factura fiscal?</strong>", "<strong>¿Expiden factura fiscal?</strong>"),
        ("<p>Si expedimos factura fiscal, mándanos tus datos.</p>",
         "<p>Sí, expedimos factura fiscal. Envíanos tus datos después de tu compra.</p>"),
        ("Dudas del Producto", "Dudas del producto"),
        ("<p>Share what your customers are saying about your products, customer service or shipping rates.</p>",
         "<p>Comparte aquí la opinión de un cliente sobre sus piezas, la atención o los envíos.</p>"),
    ],
    'templates/page.json': [
        ("nobles.A", "nobles. A"), ("lotes.Es", "lotes. Es"), ("final.En", "final. En"),
        ("Asia.Nuestra", "Asia. Nuestra"), ("local.Participamos", "local. Participamos"),
        ("Guadalajara.Esta", "Guadalajara. Esta"),
    ],
    'templates/page.nosotros.json': [
        ("rgba(NaN, NaN, NaN, 0)", "rgba(0, 0, 0, 0)"),
        ("belleza duradera</p>", "belleza duradera.</p>"),
        ("<strong>ORO</strong>", "<strong>Oro</strong>"),
        ("<p><br/><strong>Oro</strong>", "<p><strong>Oro</strong>"),
        ("<strong>El Valor de los Metales Preciosos</strong>", "<strong>El valor de los metales preciosos</strong>"),
    ],
    'sections/header-group.json': [
        ("3 MSI en toda la tienda", "3 meses sin intereses en toda la tienda"),
        ("GARANTÍA DE ORO REAL", "Garantía de oro real"),
    ],
    'sections/overlay-group.json': [
        ("Acompleta con", "Complementa tu compra con"),
        ("Signup for our newsletter", "Suscríbete a nuestras novedades"),
        ("Describe what your customers will receive when subscribing to your newsletter.",
         "Recibe antes que nadie lanzamientos, promociones y meses sin intereses."),
        ("<p>We use cookies and similar technologies to provide the best experience on our website. Refer to our Privacy Policy for more information.</p>",
         "<p>Usamos cookies y tecnologías similares para brindarte la mejor experiencia en nuestro sitio. Consulta nuestra Política de privacidad para más información.</p>"),
        ("Cookie policy", "Política de cookies"),
    ],
    'templates/page.contacto-v1-owd.json': [
        ("<p>Use this text to share information about your brand with your customers. Describe a product, share announcements, or welcome customers to your store.</p>",
         "<p>Comparte aquí información sobre Imperial Jewelry con tus clientes.</p>"),
    ],
}
FILE_EXACT = {
    'templates/product.product-page-v2.json': {
        "envío seguro": "Envío seguro", "facturación disponible": "Facturación disponible",
        "compra protegida": "Compra protegida", "¿necesitas ayuda?": "¿Necesitas ayuda?",
        "preguntas frecuentes": "Preguntas frecuentes",
    },
    'templates/page.nosotros.json': {
        "plata ley 925": "Plata Ley .925", "calidad internacional": "Calidad internacional",
        "el valor de lo auténtico": "El valor de lo auténtico",
    },
    'templates/page.faq.json': {
        "Order": "Pedidos",
        "Do you ship overseas?": "¿Hacen envíos a todo México?",
        "How long will it take to get my orders?": "¿Cuánto tarda en llegar mi pedido?",
        "Any question?": "¿Tienes otra duda?",
    },
    'templates/page.contacto-v1-owd.json': {"Subheading": "Subtítulo", "Heading": "Encabezado"},
    'sections/overlay-group.json': {"Subscribe": "Suscribirme"},
}
FILE_PREFIX = {
    'templates/page.faq.json': [
        ("<p>Yes, we ship all over the world.",
         "<p>Sí, enviamos a toda la República Mexicana. El envío es gratis en compras desde $1,999, después de descuentos; en pedidos menores cuesta $99.</p>"),
        ("<p>It depends on where you are.",
         "<p>Dentro de México, el envío estándar tarda de 3 a 5 días hábiles y es gratis en compras desde $1,999, después de descuentos. En pedidos menores a $1,999 cuesta $99. En pedidos de hasta $999 también puedes elegir envío Express ($200), que tarda de 2 a 3 días hábiles. En zonas rurales o de difícil acceso puede tardar hasta 7 días hábiles.</p><p>En cuanto sale tu pedido te enviamos por correo tu número de guía para rastrearlo.</p>"),
        ("<p>You can contact us through our contact page!",
         "<p>Escríbenos desde nuestra página de contacto. Con gusto te ayudamos.</p>"),
    ],
}
PATH_SET = {
    'templates/index.json': {
        'sections.rich_text_8xghYJ.blocks.heading_RYYEMK.settings.heading_tag': 'h2',
        'sections.featured_collections_GYrtJz.blocks.collection_NgJp6C.settings.link_text': 'Ver todo',
        'sections.featured_collections_GYrtJz.blocks.collection_pG6TTC.settings.link_text': 'Ver todo',
    },
    'templates/product.productpage.json': {
        'sections.rich_text_JtJyAH.blocks.heading_Qgjywj.settings.heading_tag': 'h2',
    },
}
STRONG_STRIP_PATHS = {
    'templates/page.json': [
        'sections.image_with_text_block_HtwG7C.blocks.richtext_pEXnyU.settings.content',
        'sections.image_with_text_block_hCGNTm.blocks.richtext_dQKKGc.settings.content',
        'sections.image_with_text_block_96EJKk.blocks.richtext_LpnHyc.settings.content',
    ],
}


def resolve(data, dotted):
    node = data
    for p in dotted.split('.'):
        node = node[p]
    return node


def set_path(data, dotted, value, fname):
    parts = dotted.split('.')
    try:
        parent = resolve(data, '.'.join(parts[:-1]))
        old = parent[parts[-1]]
    except (KeyError, TypeError):
        MISSING.append((fname, dotted))
        return
    if old != value:
        parent[parts[-1]] = value
        LOG.append((fname, dotted, old, value))


FILES = sorted(set(list(FILE_SUB) + list(FILE_EXACT) + list(FILE_PREFIX) + list(PATH_SET)
                   + list(STRONG_STRIP_PATHS)
                   + ['templates/product.json', 'templates/page.contact.json',
                      'sections/footer-group.json', 'templates/collection.json']))

for fname in FILES:
    p = os.path.join(ROOT, fname)
    if not os.path.exists(p):
        MISSING.append((fname, '<archivo completo>'))
        continue
    data = load(p)
    subs = GLOBAL_SUB + FILE_SUB.get(fname, [])
    exacts = dict(GLOBAL_EXACT)
    exacts.update(FILE_EXACT.get(fname, {}))
    prefixes = FILE_PREFIX.get(fname, [])

    def fixer(path, v, fname=fname, subs=subs, exacts=exacts, prefixes=prefixes):
        if v in exacts:
            LOG.append((fname, path, v, exacts[v]))
            return exacts[v]
        for pref, repl in prefixes:
            if v.startswith(pref):
                LOG.append((fname, path, v[:120], repl[:120]))
                return repl
        orig = v
        for a, b in subs:
            v = v.replace(a, b)
        if v != orig:
            LOG.append((fname, path, orig[:160], v[:160]))
        return v

    walk(data, 'root', fixer)
    for dotted, val in PATH_SET.get(fname, {}).items():
        set_path(data, dotted, val, fname)
    for dotted in STRONG_STRIP_PATHS.get(fname, []):
        try:
            v = resolve(data, dotted)
        except (KeyError, TypeError):
            MISSING.append((fname, dotted))
            continue
        nv = v.replace('<strong>', '').replace('</strong>', '').replace('<br/></p>', '</p>')
        if nv != v:
            set_path(data, dotted, nv, fname)
    save(p, data)

if LOG_PATH:
    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        for row in LOG:
            f.write('\t'.join(str(x).replace('\n', ' ') for x in row) + '\n')

print(f"Cambios aplicados: {len(LOG)}")
for k, c in Counter(x[0] for x in LOG).most_common():
    print(f"  {k}: {c}")
print(f"Rutas/archivos que no existen en este tema: {len(MISSING)}")
for m in MISSING:
    print("  ", m)
