"""Genera catalogo/index.html (segunda versión del catálogo) a partir de index.html.

index.html es la fuente: precios, productos y diseño se editan ahí.
Después de cada cambio, correr:  python3 build_variante.py
La variante cambia solo el WhatsApp, el texto de envíos y saca el nombre del negocio.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "https://noelicarusottidev.github.io/Promociones-Catalogo-Navidad-/"

# (texto en index.html, texto en la variante, cantidad esperada de apariciones)
CAMBIOS = [
    ("wa.me/5492214386220", "wa.me/5492214405045", 8),
    ("221 438-6220", "221 440-5045", 1),
    ("<title>Catálogo Blanquería Vanina</title>", "<title>Catálogo Navidad 2026</title>", 1),
    ('<meta property="og:site_name" content="Blanquería Vanina">\n', "", 1),
    ("✨ Blanquería Vanina · Catálogo Navidad 2026 ✨", "✨ Catálogo Navidad 2026 ✨", 1),
    (
        "Envío gratis a domicilio en todo La Plata.\">",
        "Envíos en La Plata, Berisso y alrededores.\">",
        2,
    ),
    (
        "6 productos con envío gratis a domicilio en todo La Plata.",
        "6 productos con envíos en La Plata, Berisso y alrededores.",
        1,
    ),
    (
        "🎁 Envío gratis a domicilio en todo La Plata ·",
        "🎁 Envíos en La Plata, Berisso y alrededores ·",
        1,
    ),
    (f'<meta property="og:url" content="{BASE}">', f'<meta property="og:url" content="{BASE}catalogo/">', 1),
    (f"{BASE}img/preview.jpg", f"{BASE}img/preview-catalogo.jpg", 1),
    ('"img/', '"../img/', 12),
]


def main() -> None:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    for viejo, nuevo, veces in CAMBIOS:
        hallados = html.count(viejo)
        if hallados != veces:
            raise SystemExit(f"Esperaba {veces} de {viejo!r} y encontré {hallados}")
        html = html.replace(viejo, nuevo)
    for resto in ("4386220", "438-6220", "Vanina", "gratis"):
        if resto in html:
            raise SystemExit(f"Quedó {resto!r} en la variante")
    destino = ROOT / "catalogo"
    destino.mkdir(exist_ok=True)
    (destino / "index.html").write_text(html, encoding="utf-8")
    print("catalogo/index.html generado")


if __name__ == "__main__":
    main()
